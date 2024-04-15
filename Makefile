env:
	rm -rf venv/
	python3.12 -m venv venv

deps:
	poetry install --no-root
