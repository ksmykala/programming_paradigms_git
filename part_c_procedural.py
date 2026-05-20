
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
def get_total(expenses):
    """
    Calculate the total amount of all expenses.
    Parameters:
        expenses: list of expenses
    returns:
        a float sum of all expenses.
    """
    pass
    total = 0.0
    for expense in expenses:
        total += expense["amount"]
    return total
def get_count(expenses):
    """Return the number of expense records."""
    pass
    count = 0
    for expense in expenses:
        count += 1
    return count
def get_category_totals(expenses):
    """
       Build a mapping from category names to their total amounts.

       Returns:
           dict: {category: total_amount}
       """
    pass
    totals= {}
    for expense in expenses:
        category = expense["category"]
        totals[category] = totals.get(category, 0) + expense["amount"]
    return totals
def get_most_expensive(expenses):
    """Return the expense dict with the highest amount (no max() built-in)."""
    pass
    most_expensive = expenses[0]
    for expense in expenses[1:]:
        if expense["amount"] > most_expensive["amount"]:
            most_expensive = expense
    return most_expensive
def get_least_expensive(expenses):
    """Return the expense dict with the lowest amount (no min() built-in)."""
    pass
    least_expensive = expenses[0]
    for expense in expenses[1:]:
        if expense["amount"] < least_expensive["amount"]:
            least_expensive = expense
    return least_expensive
def get_average(expenses):
    """Return the average expense amount."""
    pass
    total = get_total(expenses)
    count = get_count(expenses)
    return total / count
def get_above_average(expenses):
    """ Return a list of expense dicts whose amount is strictly above the average. """
    pass
    above_average = []
    average = get_average(expenses)
    for expense in expenses:
        if expense["amount"] > average:
            above_average.append(expense)
    return above_average
def print_summary(expenses):
    """Print the summary of all expenses using the helper function above
    Produce the same output as parts B1-B4."""
    pass
    #B1
    print(f"Total spending: {get_total(expenses)}")
    print(f"Number of expenses: {get_count(expenses)}")
    print()
    #B2
    print("Category breakdown")
    category_totals = get_category_totals(expenses)
    for category,total in category_totals.items():
        print(f"{category}: {total}")
    print()
    #B3
    most = get_most_expensive(expenses)
    least = get_least_expensive(expenses)
    print(f"Most expensive: {most['description']} ({most['category']}) {most['amount']}")
    print(f"Least expensive: {least['description']} ({least['category']}) {least['amount']}")
    print()
    #B4
    average = get_average(expenses)
    above = get_above_average(expenses)
    print(f"Average: {average}")
    for item in above:
        print(f"- {item['description']}  {item['amount']}")
print_summary(expenses)