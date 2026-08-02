const entryActions = [
  "Write one falsifiable prediction before opening any implementation.",
  "Run one failing test and name the earliest violated invariant.",
  "Calculate one attention-score row by hand.",
  "State the shape and causal role of one tensor aloud.",
  "Delete one vague sentence and replace it with an equation plus intervention.",
  "Open today’s source stub and implement only the first TODO.",
  "Explain one mechanism for five minutes without notes or anthropomorphic words.",
  "Change one controlled variable and predict the direction of the result.",
];

let days = [];
let progress = null;
let secondsLeft = 45 * 60;
let timerHandle = null;

const el = (id) => document.getElementById(id);
const pad = (n) => String(n).padStart(2, "0");

async function loadData() {
  const [dayResponse, progressResponse] = await Promise.all([
    fetch("days.json", { cache: "no-store" }),
    fetch("progress.json", { cache: "no-store" }),
  ]);
  if (!dayResponse.ok || !progressResponse.ok) throw new Error("Could not load forge data");
  const dayIndex = await dayResponse.json();
  progress = await progressResponse.json();
  days = dayIndex.days;
  render();
}

function render() {
  const completed = new Set(progress.completed_days || []);
  const floors = new Set(progress.floor_days || []);
  const currentDay = Math.min(Number(progress.current_day || 1), 14);
  const current = days.find((day) => day.day === currentDay) || days[days.length - 1];
  const percentage = Math.round((completed.size / 14) * 100);

  el("days-complete").textContent = completed.size;
  el("current-day-number").textContent = pad(currentDay);
  el("completion-percent").textContent = `${percentage}%`;
  el("floor-count").textContent = floors.size;
  el("progress-fill").style.width = `${percentage}%`;
  el("program-state").textContent = completed.size === 14 ? "FORGE COMPLETE" : `GATE ${pad(currentDay)} OPEN`;

  el("mission-title").textContent = current.title;
  el("mission-day").textContent = `DAY ${pad(current.day)}`;
  el("mission-core").textContent = current.core;
  el("mission-file").href = `../${current.file}`;
  el("mission-command").textContent = `make start DAY=${current.day}`;
  el("dialog-floor").textContent = `make floor DAY=${current.day}`;

  const build = el("days-grid-build");
  const open = el("days-grid-open");
  build.replaceChildren();
  open.replaceChildren();

  days.forEach((day) => {
    const card = document.createElement("a");
    const isComplete = completed.has(day.day);
    const isCurrent = day.day === currentDay && !isComplete;
    const isLocked = day.day > currentDay;
    card.className = `day-card${isComplete ? " complete" : ""}${isCurrent ? " current" : ""}${isLocked ? " locked" : ""}`;
    card.href = `../${day.file}`;
    card.innerHTML = `
      <div class="day-card-head">
        <span>DAY ${pad(day.day)}</span>
        <span class="day-card-state" aria-hidden="true"></span>
      </div>
      <h3>${day.title}</h3>
      <p>${day.core}</p>
      <footer>${isComplete ? "PROVED" : isCurrent ? "GATE OPEN" : "VISIBLE · NOT UNLOCKED"}</footer>
    `;
    (day.day <= 7 ? build : open).appendChild(card);
  });
}

function renderTimer() {
  const minutes = Math.floor(secondsLeft / 60);
  const seconds = secondsLeft % 60;
  el("timer").textContent = `${pad(minutes)}:${pad(seconds)}`;
  document.title = timerHandle ? `${pad(minutes)}:${pad(seconds)} · Forge` : "LLM Mechanism Forge";
}

function toggleTimer() {
  if (timerHandle) {
    clearInterval(timerHandle);
    timerHandle = null;
    el("timer-toggle").textContent = "Resume";
    renderTimer();
    return;
  }
  el("timer-toggle").textContent = "Pause";
  timerHandle = setInterval(() => {
    secondsLeft -= 1;
    if (secondsLeft <= 0) {
      secondsLeft = 0;
      clearInterval(timerHandle);
      timerHandle = null;
      el("timer-toggle").textContent = "Complete";
      if ("Notification" in window && Notification.permission === "granted") {
        new Notification("First hard block complete", { body: "Record what you predicted, built and falsified." });
      }
    }
    renderTimer();
  }, 1000);
  if ("Notification" in window && Notification.permission === "default") Notification.requestPermission();
}

function resetTimer() {
  clearInterval(timerHandle);
  timerHandle = null;
  secondsLeft = 45 * 60;
  el("timer-toggle").textContent = "Start";
  renderTimer();
}

function randomEntryAction() {
  return entryActions[Math.floor(Math.random() * entryActions.length)];
}

function setEntryAction() {
  const action = randomEntryAction();
  el("entry-action").textContent = action;
  el("dialog-action").textContent = action;
}

function wireEvents() {
  el("timer-toggle").addEventListener("click", toggleTimer);
  el("timer-reset").addEventListener("click", resetTimer);
  el("new-entry-action").addEventListener("click", setEntryAction);
  el("avoidance-button").addEventListener("click", () => {
    setEntryAction();
    el("avoidance-dialog").showModal();
  });
  el("dialog-close").addEventListener("click", () => el("avoidance-dialog").close());
  el("avoidance-dialog").addEventListener("click", (event) => {
    if (event.target === el("avoidance-dialog")) el("avoidance-dialog").close();
  });
}

wireEvents();
renderTimer();
loadData().catch((error) => {
  console.error(error);
  el("mission-title").textContent = "Run the dashboard through `make dashboard`";
  el("mission-core").textContent = "Browsers block local JSON loading from file://. Serve the repository and open http://localhost:8000/docs/.";
});
