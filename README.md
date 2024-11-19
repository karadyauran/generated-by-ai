# Personal Finance Tracker

Welcome to the Personal Finance Tracker - a command-line interface application designed to help you manage and track your personal finances effectively.

## Features
- **Transaction Management**: Easily add, view, and manage your income and expense transactions.
- **Budgeting**: Set and maintain budgets across various categories.
- **Reports**: Generate insightful reports on your financial health.
- **Secure Storage**: Transactions are securely stored using SQLite, with a file-based option for backup.

## Installation

Ensure you have Python 3 installed on your system. Clone the repository and navigate into the project directory:

```bash
$ git clone https://github.com/your-repository/personal-finance-tracker.git
$ cd personal-finance-tracker
```

Install the required dependencies:

```bash
$ pip install -r requirements.txt
```

## Usage

Start the application by running the following command:

```bash
$ python3 src/main.py
```

Follow the prompts in the command-line interface to utilize the various features.

## Project Structure
- **src/domain**: Contains core business logic for transactions and budgets.
- **src/services**: Provides services for managing transactions and budgets.
- **src/adapters**: Handles database and file storage operations.
- **src/utils**: Utility functions to assist with common operations.
- **src/interfaces**: User interface for interacting with the application through CLI.

## Contributing
If you'd like to contribute to this project, please fork the repository and use a feature branch. Pull requests are warmly welcome.

## License
This project is licensed under the MIT License.

---

Project created by OpenAI API.
