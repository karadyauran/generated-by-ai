def print_menu(options):
    """
    Print a list of options as a menu.
    :param options: A list of menu options.
    """
    for idx, option in enumerate(options, 1):
        print(f"{idx}. {option}")


def get_user_choice(menu_size):
    """
    Prompt the user to select an option from the menu.
    :param menu_size: The number of available options.
    :return: The index chosen by the user.
    """
    while True:
        try:
            choice = int(input("Enter the menu option number: "))
            if 1 <= choice <= menu_size:
                return choice
            else:
                print("Invalid choice. Please choose a valid option.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def convert_currency(amount, rate):
    """
    Convert an amount to another currency using a specified rate.
    :param amount: The amount in original currency.
    :param rate: Conversion rate to the target currency.
    :return: The converted amount.
    """
    return amount * rate


def format_currency(amount, currency_symbol='$'):
    """
    Format an amount with the given currency symbol.
    :param amount: The numeric currency value.
    :param currency_symbol: The symbol of the currency to prepended.
    :return: String representing the formatted currency.
    """
    return f"{currency_symbol}{amount:,.2f}"


def validate_transaction_input(prompt, data_type=int):
    """
    Validate user input for transactions ensuring it's the correct data type.
    :param prompt: The message displayed to the user.
    :param data_type: The type of data expected (e.g., int, float).
    :return: The validated user input of the desired type.
    """
    while True:
        try:
            return data_type(input(prompt))
        except ValueError:
            print(f"Please enter a valid {data_type.__name__}.")


def notify_budget_exceeded(category, amount):
    """
    Prints a notification that the budget has been exceeded for a category.
    :param category: The category name.
    :param amount: The exceeding amount value.
    """
    print(f"Warning: You have exceeded your budget for {category} by {format_currency(amount)}!")
