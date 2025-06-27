PYTHON=python
BOT_SCRIPT=bot/main.py


export PYTHONPATH := .

run:
	@echo "Running bot..."
	@$(PYTHON) $(BOT_SCRIPT)