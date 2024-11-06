# Personal Finance Tracker

![Personal Finance Tracker Logo](logo.png)

## Overview
The Personal Finance Tracker is a console-based application that allows users to manage their financial transactions, set budgets, and generate insightful reports. The application is built using Python with a focus on clean architecture principles to ensure scalability and maintainability.

## Features
- Add and view financial transactions by category.
- Set and manage financial budgets for various spending categories.
- Generate comprehensive reports to analyze income and expenses.
- User authentication for data security.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/username/personal-finance-tracker.git
   cd personal-finance-tracker
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Configure your environment variables:
   ```bash
   cp config/.env.example .env
   # Edit the .env file with real credentials and settings
   ```

## Usage
Run the application using:
```bash
python src/main.py
```

## Testing
To run the tests, execute:
```bash
pytest
```

## Development
Lint your code to maintain quality:
```bash
flake8 src/
```

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

### Note
This project was created using OpenAI's GPT-3 API.
