PYTHON=python
BOT_SCRIPT=main.py

export PYTHONPATH := .

run:
	@echo "Running bot..."
	@$(PYTHON) $(BOT_SCRIPT)