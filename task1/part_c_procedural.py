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


def get_total(expense_list):
    """
    Calculate the total amount of all expenses.

    Parameters:
        expense_list (list): List of expense dictionaries.

    Returns:
        float: Sum of all 'amount' values.
    """
    total = 0
    for e in expense_list:
        total += e["amount"]
    return total


def get_count(expense_list):
    """Return the number of expense records."""
    count = 0
    for _ in expense_list:
        count += 1
    return count


def get_category_totals(expense_list):
    """
    Build a mapping from category names to their total amounts.

    Returns:
        dict: {category: total_amount}
    """
    totals = {}
    for e in expense_list:
        cat = e["category"]
        if cat not in totals:
            totals[cat] = 0
        totals[cat] += e["amount"]
    return totals


def get_most_expensive(expense_list):
    """Return the expense dict with the highest amount (no max() built-in)."""
    # Assume list is non-empty, as per assignment data
    max_amount = expense_list[0]["amount"]
    most = expense_list[0]
    for e in expense_list[1:]:
        if e["amount"] > max_amount:
            max_amount = e["amount"]
            most = e
    return most


def get_least_expensive(expense_list):
    """Return the expense dict with the lowest amount (no min() built-in)."""
    min_amount = expense_list[0]["amount"]
    least = expense_list[0]
    for e in expense_list[1:]:
        if e["amount"] < min_amount:
            min_amount = e["amount"]
            least = e
    return least


def get_average(expense_list):
    """Return the average expense amount as a float."""
    total = 0
    count = 0
    for e in expense_list:
        total += e["amount"]
        count += 1
    return total / count


def get_above_average(expense_list):
    """
    Return a list of expense dicts whose amount is strictly above the average.
    """
    avg = get_average(expense_list)
    above = []
    for e in expense_list:
        if e["amount"] > avg:
            above.append(e)
    return above


def print_summary(expense_list):
    """
    Print a full summary report using the helper functions above.
    Produce the same output as Parts B1–B4 combined.
    """
    total = get_total(expense_list)
    count = get_count(expense_list)
    print(f"Total expenses: {total:.2f}")
    print(f"Number of records: {count}")

    cat_totals = get_category_totals(expense_list)
    print("\nCategory breakdown:")
    for cat in sorted(cat_totals.keys()):
        print(f"  {cat} : {cat_totals[cat]:.2f}")

    most = get_most_expensive(expense_list)
    least = get_least_expensive(expense_list)
    print(f"\nMost expensive : {most['description']} ({most['category']}) — {most['amount']:.2f}")
    print(f"Least expensive: {least['description']} ({least['category']}) — {least['amount']:.2f}")

    avg = get_average(expense_list)
    above = get_above_average(expense_list)
    print(f"\nAverage expense: {avg:.2f}")
    print("Expenses above average:")
    for e in above:
        print(f"  - {e['description']} ({e['amount']:.2f})")


if __name__ == "__main__":
    print_summary(expenses)
