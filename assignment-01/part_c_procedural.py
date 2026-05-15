# -*- coding: windows-1250 -*-
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
    """Return total amount of all expenses."""
    total = 0
    for e in expense_list:
        total += e["amount"]
    return total

def get_count(expense_list):
    """Return number of expense records."""
    return len(expense_list)

def get_category_totals(expense_list):
    """Return dict {category: total_amount}."""
    totals = {}
    for e in expense_list:
        cat = e["category"]
        amt = e["amount"]
        totals[cat] = totals.get(cat, 0) + amt
    return totals

def get_most_expensive(expense_list):
    """Return expense dict with highest amount (no max())."""
    if not expense_list:
        return None
    most = expense_list[0]
    for e in expense_list:
        if e["amount"] > most["amount"]:
            most = e
    return most

def get_least_expensive(expense_list):
    """Return expense dict with lowest amount (no min())."""
    if not expense_list:
        return None
    least = expense_list[0]
    for e in expense_list:
        if e["amount"] < least["amount"]:
            least = e
    return least

def get_average(expense_list):
    """Return average expense amount."""
    total = get_total(expense_list)
    count = get_count(expense_list)
    return total / count if count != 0 else 0

def get_above_average(expense_list):
    """Return list of expense dicts with amount > average."""
    avg = get_average(expense_list)
    result = []
    for e in expense_list:
        if e["amount"] > avg:
            result.append(e)
    return result

def print_summary(expense_list):
    """Print full report using helper functions."""
    # B1
    total = get_total(expense_list)
    count = get_count(expense_list)
    print(f"Total expenses: {total:.2f}")
    print(f"Number of records: {count}")
    # B2
    cat_totals = get_category_totals(expense_list)
    print("\nCategory breakdown:")
    for cat in sorted(cat_totals.keys()):
        print(f"  {cat:15} : {cat_totals[cat]:.2f}")
    # B3
    most = get_most_expensive(expense_list)
    least = get_least_expensive(expense_list)
    print(f"\nMost expensive : {most['description']} ({most['category']}) — {most['amount']:.2f}")
    print(f"Least expensive: {least['description']} ({least['category']}) — {least['amount']:.2f}")

    # B4
    avg = get_average(expense_list)
    above = get_above_average(expense_list)
    print(f"\nAverage expense: {avg:.2f}")
    print("Expenses above average:")
    for e in above:
        print(f"  - {e['description']} ({e['amount']:.2f})")

if __name__ == "__main__":
    print_summary(expenses)