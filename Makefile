run:
	@python src/app/UI.py

frmt:
	@python -m black $(shell find . -type f -name "*.py")
