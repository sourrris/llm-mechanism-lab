#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import os
import random
import shutil
import subprocess
import sys
from datetime import date, datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INDEX_PATH = ROOT / "curriculum" / "index.json"
PROGRESS_PATH = ROOT / "progress.json"
TEMPLATES = ROOT / "templates"

COMMON_EVIDENCE = {
    "daily-log.md": 250,
    "predictions.md": 180,
    "explanation.md": 450,
    "oral-defense.md": 250,
}
SPECIAL_EVIDENCE = {
    2: {"tokenizer-report.md": 350},
    3: {"manual-attention.md": 300},
    4: {"block-diagram.md": 250},
    5: {"shape-trace.md": 300},
    6: {"training-curve.csv": 40, "bug-autopsy.md": 300},
    7: {"decoding-grid.md": 500, "week-one-defense.md": 500},
    8: {"diagnosis.md": 1200},
    9: {"activation-summary.md": 500, "logit-lens.csv": 60},
    10: {"patching-analysis.md": 700, "patching-result.png": 1},
    11: {"circuit-report.md": 900},
    12: {"checkpoint-comparison.md": 700},
    13: {"mini-study.md": 1200, "results.csv": 80},
    14: {"final-defense.md": 1200},
}

FIVE_MINUTE_ACTIONS = [
    "Write one falsifiable prediction before opening any implementation.",
    "Run one failing test and name the earliest violated invariant.",
    "Calculate one attention-score row by hand.",
    "State the shape and causal role of one tensor aloud.",
    "Open today's first TODO and write only the inputs, output and equation.",
]


def load_index() -> dict:
    return json.loads(INDEX_PATH.read_text(encoding="utf-8"))


def default_progress() -> dict:
    return {
        "program": "LLM Mechanism Forge",
        "start_date": "2026-08-03",
        "current_day": 1,
        "completed_days": [],
        "floor_days": [],
        "completion_log": {},
        "last_completed": None,
    }


def load_progress() -> dict:
    if not PROGRESS_PATH.exists():
        save_progress(default_progress())
    return json.loads(PROGRESS_PATH.read_text(encoding="utf-8"))


def save_progress(progress: dict) -> None:
    PROGRESS_PATH.write_text(json.dumps(progress, indent=2) + "\n", encoding="utf-8")
    docs_progress = ROOT / "docs" / "progress.json"
    docs_progress.write_text(json.dumps(progress, indent=2) + "\n", encoding="utf-8")


def day_record(day: int) -> dict:
    for item in load_index()["days"]:
        if item["day"] == day:
            return item
    raise SystemExit(f"Day must be 1..14, received {day}")


def evidence_dir(day: int) -> Path:
    return ROOT / "evidence" / f"day-{day:02d}"


def start_day(day: int) -> None:
    record = day_record(day)
    target = evidence_dir(day)
    target.mkdir(parents=True, exist_ok=True)
    templates = {
        "daily-log.md": "daily-log.md",
        "predictions.md": "predictions.md",
        "explanation.md": "explanation.md",
        "oral-defense.md": "oral-defense.md",
    }
    for destination, template in templates.items():
        path = target / destination
        if not path.exists():
            body = (TEMPLATES / template).read_text(encoding="utf-8")
            path.write_text(f"<!-- Day {day:02d}: {record['title']} -->\n\n" + body, encoding="utf-8")
    for filename in SPECIAL_EVIDENCE.get(day, {}):
        path = target / filename
        if not path.exists():
            if path.suffix == ".png":
                continue
            path.write_text(f"# Day {day:02d} — {filename}\n\n", encoding="utf-8")
    print(f"Started Day {day:02d}: {record['title']}")
    print(f"Mission: {record['core']}")
    print(f"Open: {record['file']}")
    print(f"Evidence: {target.relative_to(ROOT)}")


def meaningful_size(path: Path) -> int:
    """Count user-authored evidence, not prefilled template scaffolding."""
    if path.suffix.lower() == ".png":
        return path.stat().st_size if path.exists() else 0
    text = path.read_text(encoding="utf-8") if path.exists() else ""
    useful_lines: list[str] = []
    for raw in text.splitlines():
        line = raw.strip()
        if not line or line.startswith(("#", "<!--")):
            continue
        if line.startswith("|"):
            cells = [cell.strip() for cell in line.strip("|").split("|")]
            if not cells or all(not cell or set(cell) <= {"-", ":", "%"} for cell in cells):
                continue
            # Empty table rows and the fixed prediction-table headings are scaffolding.
            if cells[0].isdigit() and all(not cell or cell == "%" for cell in cells[1:]):
                continue
            if cells[0] in {"#", "Date", "Claim", "Case", "Metric", "Checkpoint"}:
                continue
        lowered = line.lower()
        if lowered.startswith((
            "write before", "do not delete", "observation / association",
            "reading, watching", "the floor prevents", "copy this template",
        )):
            continue
        if line.startswith("-"):
            value = line[1:].strip()
            if not value or value.endswith(":") or value in {
                "Energy (1–10):", "Resistance (1–10):", "Exact first hard action:",
                "Distraction placed in PARKING_LOT.md:", "Symptom:",
                "Earliest incorrect assumption or operation:", "Cause:",
                "Correction:", "Prevention/test added:", "Core gate passed? No",
                "Bad-day floor used? No", "Commit:", "Next unresolved step:",
                "Derivation /20", "Shapes /20", "Causal mechanism /20",
                "Intervention /20", "Uncertainty discipline /20", "Total /100",
                "H1:", "H2:",
            }:
                continue
        useful_lines.append(line)
    return len("\n".join(useful_lines).strip())


def evidence_errors(day: int) -> list[str]:
    target = evidence_dir(day)
    errors: list[str] = []
    requirements = dict(COMMON_EVIDENCE)
    requirements.update(SPECIAL_EVIDENCE.get(day, {}))
    for filename, minimum in requirements.items():
        path = target / filename
        if not path.exists():
            errors.append(f"missing {path.relative_to(ROOT)}")
            continue
        size = meaningful_size(path)
        if size < minimum:
            errors.append(f"{path.relative_to(ROOT)} has {size} meaningful bytes; requires {minimum}")
    if day == 14:
        atlas = ROOT / "mechanism-atlas" / "final-atlas.md"
        if not atlas.exists() or meaningful_size(atlas) < 2500:
            errors.append("mechanism-atlas/final-atlas.md requires at least 2500 meaningful bytes")
    return errors


def run_tests(day: int) -> bool:
    test_dir = ROOT / "tests" / f"day{day:02d}"
    if not test_dir.exists():
        print("No automated unit tests for this day.")
        return True
    env = os.environ.copy()
    env["PYTHONPATH"] = str(ROOT / "src") + os.pathsep + env.get("PYTHONPATH", "")
    result = subprocess.run(
        [sys.executable, "-m", "pytest", "-q", str(test_dir)],
        cwd=ROOT,
        env=env,
        check=False,
    )
    return result.returncode == 0


def check_day(day: int, run_code_tests: bool = True) -> bool:
    print(f"Checking Day {day:02d}…")
    errors = evidence_errors(day)
    for error in errors:
        print(f"  ✗ {error}")
    tests_ok = run_tests(day) if run_code_tests else True
    if errors or not tests_ok:
        print("\nGate failed. Fix the earliest failure; do not restart the day.")
        return False
    print("  ✓ evidence gate")
    if tests_ok:
        print("  ✓ executable gate")
    print("Day gate passed.")
    return True


def complete_day(day: int) -> None:
    progress = load_progress()
    current = int(progress["current_day"])
    if day != current:
        raise SystemExit(f"Current gate is Day {current:02d}; complete it before Day {day:02d}.")
    if not check_day(day):
        raise SystemExit(1)
    completed = sorted(set(progress.get("completed_days", [])) | {day})
    progress["completed_days"] = completed
    now = datetime.now().astimezone().isoformat(timespec="seconds")
    progress["completion_log"][str(day)] = now
    progress["last_completed"] = now
    progress["current_day"] = min(15, day + 1)
    save_progress(progress)
    print(f"\nDay {day:02d} recorded complete.")
    if day < 14:
        next_day = day_record(day + 1)
        print(f"Next: Day {day + 1:02d} — {next_day['title']}")
    else:
        print("Forge complete. Begin one 30-day original research cycle; do not restart Day 1.")


def mark_floor(day: int) -> None:
    progress = load_progress()
    floors = sorted(set(progress.get("floor_days", [])) | {day})
    progress["floor_days"] = floors
    save_progress(progress)
    print(f"Recorded bad-day floor for Day {day:02d}. The core gate remains open.")


def show_status() -> None:
    progress = load_progress()
    completed = set(progress.get("completed_days", []))
    floor = set(progress.get("floor_days", []))
    cells = []
    for day in range(1, 15):
        if day in completed:
            cells.append("██")
        elif day in floor:
            cells.append("▒▒")
        elif day == progress.get("current_day"):
            cells.append("▶ ")
        else:
            cells.append("··")
    print("LLM Mechanism Forge")
    print(" ".join(cells))
    print(f"Completed: {len(completed)}/14")
    current = int(progress.get("current_day", 1))
    if current <= 14:
        record = day_record(current)
        print(f"Current: Day {current:02d} — {record['title']}")
    else:
        print("Current: 14-day forge complete")
    if floor:
        print("Floor recorded (not complete): " + ", ".join(f"{d:02d}" for d in sorted(floor - completed)))


def show_today() -> None:
    progress = load_progress()
    day = int(progress.get("current_day", 1))
    if day > 14:
        print("The 14-day forge is complete. Work from your next 30-day research question.")
        return
    record = day_record(day)
    print(f"DAY {day:02d} — {record['title']}")
    print(f"Scheduled date: {record['date']} (Asia/Kolkata)")
    print(f"Mission: {record['core']}")
    print(f"\nBad-day floor: {record['floor']}")
    print(f"\nOpen {record['file']}")
    print(f"Start with: make start DAY={day}")


def recover() -> None:
    progress = load_progress()
    day = min(int(progress.get("current_day", 1)), 14)
    record = day_record(day)
    print("RECOVERY MODE")
    print("1. Do not restart or redesign the plan.")
    print("2. Open only today's curriculum and evidence folder.")
    print(f"3. Five-minute action: {random.choice(FIVE_MINUTE_ACTIONS)}")
    print(f"4. Today's floor: {record['floor']}")
    print(f"5. Record floor with: python scripts/forge.py floor {day}")
    print("6. Resume the core gate at the earliest failed test when capacity returns.")


def ci() -> None:
    progress = load_progress()
    completed = sorted(progress.get("completed_days", []))
    all_ok = True
    for day in completed:
        if not check_day(int(day)):
            all_ok = False
    if not all_ok:
        raise SystemExit(1)
    print(f"CI validated {len(completed)} completed day(s).")


def main() -> None:
    parser = argparse.ArgumentParser(description="LLM Mechanism Forge progress and evidence gate")
    sub = parser.add_subparsers(dest="command", required=True)
    for name in ("start", "check", "complete", "floor"):
        p = sub.add_parser(name)
        p.add_argument("day", type=int)
    sub.add_parser("today")
    sub.add_parser("status")
    sub.add_parser("recover")
    sub.add_parser("ci")
    args = parser.parse_args()
    if args.command == "start": start_day(args.day)
    elif args.command == "check": raise SystemExit(0 if check_day(args.day) else 1)
    elif args.command == "complete": complete_day(args.day)
    elif args.command == "floor": mark_floor(args.day)
    elif args.command == "today": show_today()
    elif args.command == "status": show_status()
    elif args.command == "recover": recover()
    elif args.command == "ci": ci()


if __name__ == "__main__":
    main()
