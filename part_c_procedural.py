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
    total = 0
    for exp in expense_list:
        total += exp["amount"]
    return total

def get_count(expense_list):
    return len(expense_list)

def get_category_totals(expense_list):
    totals = {}
    for exp in expense_list:
        cat = exp["category"]
        totals[cat] = totals.get(cat, 0) + exp["amount"]
    return totals

def get_most_expensive(expense_list):
    most = expense_list[0]
    for exp in expense_list[1:]:
        if exp["amount"] > most["amount"]:
            most = exp
    return most

def get_least_expensive(expense_list):
    least = expense_list[0]
    for exp in expense_list[1:]:
        if exp["amount"] < least["amount"]:
            least = exp
    return least

def get_average(expense_list):
    total = 0
    count = 0
    for exp in expense_list:
        total += exp["amount"]
        count += 1
    return total / count

def get_above_average(expense_list):
    avg = get_average(expense_list)
    above = []
    for exp in expense_list:
        if exp["amount"] > avg:
            above.append(exp)
    return above

def print_summary(expense_list):

    total = get_total(expense_list)
    count = get_count(expense_list)
    print(f"Total expenses: {total:}")
    print(f"Number of records: {count}")

    cat_totals = get_category_totals(expense_list)
    print("\nCategory breakdown:")
    for category in sorted(cat_totals):
        print(f"  {category:<14}: {cat_totals[category]:}")

    most = get_most_expensive(expense_list)
    least = get_least_expensive(expense_list)
    print(f"\nMost expensive : {most['description']} ({most['category']}) — {most['amount']:}")
    print(f"Least expensive: {least['description']} ({least['category']}) — {least['amount']:}")

    avg = get_average(expense_list)
    above = get_above_average(expense_list)
    print(f"\nAverage expense: {avg:}")
    print("Expenses above average:")
    for exp in above:
        print(f"  - {exp['description']} ({exp['amount']:})")


if __name__ == "__main__":
    print_summary(expenses)