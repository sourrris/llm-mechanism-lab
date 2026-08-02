PYTHON ?= python3
DAY ?= 1

.PHONY: setup today start check complete floor status recover ci dashboard interp

setup:
	./scripts/bootstrap.sh

today:
	$(PYTHON) scripts/forge.py today

start:
	$(PYTHON) scripts/forge.py start $(DAY)

check:
	$(PYTHON) scripts/forge.py check $(DAY)

complete:
	$(PYTHON) scripts/forge.py complete $(DAY)

floor:
	$(PYTHON) scripts/forge.py floor $(DAY)

status:
	$(PYTHON) scripts/forge.py status

recover:
	$(PYTHON) scripts/forge.py recover

ci:
	$(PYTHON) scripts/forge.py ci

dashboard:
	@echo "Open http://localhost:8000/docs/"
	$(PYTHON) -m http.server 8000

interp:
	$(PYTHON) -m pip install -e '.[interpretability]'
