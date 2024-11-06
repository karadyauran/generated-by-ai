# Expense Tracker

## Overview

The Expense Tracker is a console-based application developed in Python, enabling users to manage their personal finances by tracking incomes and expenses. Users can generate financial reports and receive alerts when their spending exceeds set budget limits.

## Features

- **User Registration and Authentication**: Securely create accounts and log in using hashed passwords.
- **Transaction Management**: Add, update, and delete income and expense entries.
- **Financial Reporting**: Generate monthly summary reports.
- **Budget Alerts**: Receive notifications when expenditures surpass budget constraints.

## Installation

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd expense-tracker
   ```

2. **Virtual Environment (Recommended)**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

- Run the application:
  ```bash
  python src/main.py
  ```

## Project Structure

- `src/` : Main application source code.
- `tests/` : Unit tests for the application.

## Scripts

- **Start Application**: `npm run start`
- **Test**: `npm run test`
- **Lint**: `npm run lint`

## Development

- **Run Tests**:
  ```bash
  pytest tests/
  ```

## Contributing

Please refer to the [CONTRIBUTING.md](./CONTRIBUTING.md) file for contribution guidelines.

## License

This project, created by OpenAI API, is licensed under the MIT License.

---
This README is part of the application documentation guiding users through setting up and using the Expense Tracker.