# Makefile for the project
.PHONY: install run

# Install project dependencies
install:
	@echo "Installing dependencies..."
	python3.10 -m venv .venv
	.venv/bin/pip3 install -r requirements.txt

# Run the main script
run:
	@echo "Running the app"
	.venv/bin/python3 streamlit run main.py