# Makefile for managing the Book Recommender Hub project

.PHONY: all clean install test run lint

# Default target
all: install lint test run

# Install project dependencies
install:
	@echo "Installing dependencies..."
	pip install -r requirements.txt

# Run tests
# Uses unittest to discover and run tests
# from the tests directory

test:
	@echo "Running tests..."
	python -m unittest discover -s tests

# Run the application
run:
	@echo "Starting the application..."
	python src/main.py

# Lint the project using flake8
lint:
	@echo "Linting code..."
	flake8 src

# Clean up any generated files
clean:
	@echo "Cleaning up..."
	find . -type f -name '*.pyc' -delete
	find . -type d -name '__pycache__' -delete