expenses = [
    {"date": "2024-01-05", "category": "Food",          "amount": 42.50, "description": "Groceries"},
    {"date": "2024-01-07", "category": "Transport",     "amount": 15.00, "description": "Bus pass"},
    {"date": "2024-01-09", "category": "Entertainment", "amount": 60.00, "description": "Concert ticket"},
    {"date": "2024-01-10", "category": "Food",          "amount": 8.75,  "description": "Coffee & snack"},
    {"date": "2024-01-12", "category": "Utilities",     "amount": 120.00,"description": "Electricity bill"},
    {"date": "2024-01-14", "category": "Food",          "amount": 55.20, "description": "Restaurant dinner"},
    {"date": "2024-01-15", "category": "Transport",     "amount": 30.00, "description": "Taxi"},
    {"date": "2024-01-17", "category": "Entertainment", "amount": 14.99, "description": "Streaming subscription"},
    {"date": "2024-01-20", "category": "Food",          "amount": 38.00, "description": "Groceries"},
    {"date": "2024-01-22", "category": "Utilities",     "amount": 45.00, "description": "Internet bill"},
    {"date": "2024-01-25", "category": "Transport",     "amount": 22.00, "description": "Train ticket"},
    {"date": "2024-01-28", "category": "Entertainment", "amount": 25.00, "description": "Book"},
]

# Part C — Procedural Refactoring

def get_total(expense_list):
    """
    Calculate the total amount of all expenses.

    Parameters:
        expense_list (list): List of expense dictionaries.

    Returns:
        float: Sum of all expense amounts.
    """
    total = 0

    for expense in expense_list:
        total += expense["amount"]

    return total


def get_count(expense_list):
    """
    Return the number of expense records.

    Parameters:
        expense_list (list): List of expense dictionaries.

    Returns:
        int: Number of expense records.
    """
    count = 0

    for expense in expense_list:
        count += 1

    return count


def get_category_totals(expense_list):
    """
    Build a mapping from category names to their total amounts.

    Parameters:
        expense_list (list): List of expense dictionaries.

    Returns:
        dict: Dictionary in the format {category: total_amount}.
    """
    category_totals = {}

    for expense in expense_list:
        category = expense["category"]
        amount = expense["amount"]

        if category in category_totals:
            category_totals[category] += amount
        else:
            category_totals[category] = amount

    return category_totals


def get_most_expensive(expense_list):
    """
    Return the expense dict with the highest amount (no max() built-in).

    Parameters:
        expense_list (list): List of expense dictionaries.

    Returns:
        dict: Expense with the highest amount.
    """
    max_item = expense_list[0]

    for i in range(1, len(expense_list)):
        current = expense_list[i]

        if current["amount"] > max_item["amount"]:
            max_item = current

    return max_item


def get_least_expensive(expense_list):
    """
    Return the expense dict with the lowest amount (no min() built-in).

    Parameters:
        expense_list (list): List of expense dictionaries.

    Returns:
        dict: Expense with the lowest amount.
    """
    min_item = expense_list[0]

    for i in range(1, len(expense_list)):
        current = expense_list[i]

        if current["amount"] < min_item["amount"]:
            min_item = current

    return min_item


def get_average(expense_list):
    """
    Return the average expense amount as a float.

    Parameters:
        expense_list (list): List of expense dictionaries.

    Returns:
        float: The average expense amount as a float.
    """
    total = get_total(expense_list)
    count = get_count(expense_list)

    return total / count


def get_above_average(expense_list):
    """
    Return a list of expense dicts whose amount is strictly above the average.

    Parameters:
        expense_list (list): List of expense dictionaries.

    Returns:
        list: A list of expense dicts whose amount is strictly above the average.
    """
    average = get_average(expense_list)
    above_average = []

    for expense in expense_list:
        if expense["amount"] > average:
            above_average.append(expense)

    return above_average


def print_summary(expense_list):
    """
    Print a full summary report using the helper functions above. Same output as Parts B1–B4 combined.

    Parameters:
        expense_list (list): List of expense dictionaries.

    Returns:
        None
    """

    # B1 — Total and count
    total = get_total(expense_list)
    count = get_count(expense_list)

    print(f"Total expenses: {total:.2f}")
    print(f"Number of records: {count}")

    # B2 — Category breakdown
    category_totals = get_category_totals(expense_list)

    print("\nCategory breakdown:")

    categories = list(category_totals.keys())
    categories.sort()

    for category in categories:
        print(" ", category, ":", format(category_totals[category], ".2f"))

    # B3 — Most and least expensive
    max_item = get_most_expensive(expense_list)
    min_item = get_least_expensive(expense_list)

    print(
        "\nMost expensive :",
        max_item["description"],
        f"({max_item['category']})",
        "—",
        format(max_item["amount"], ".2f")
    )

    print(
        "Least expensive:",
        min_item["description"],
        "(" + min_item["category"] + ")",
        "—",
        format(min_item["amount"], ".2f")
    )

    # B4 — Expenses above average
    average = get_average(expense_list)

    print("\nAverage expense:", format(average, ".2f"))
    print("Expenses above average:")

    above_average = get_above_average(expense_list)

    for expense in above_average:
        print(
            "  -",
            expense["description"],
            "(" + format(expense["amount"], ".2f") + ")"
        )

# Entry point
if __name__ == "__main__":
    print_summary(expenses)