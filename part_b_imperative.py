expenses = [
    {"date": "2024-01-05", "category": "Food", "amount": 42.50, "description": "Groceries"},
    {"date": "2024-01-07", "category": "Transport", "amount": 15.00, "description": "Bus pass"},
    {"date": "2024-01-09", "category": "Entertainment", "amount": 60.00, "description": "Concert ticket"},
    {"date": "2024-01-10", "category": "Food", "amount": 8.75, "description": "Coffee & snack"},
    {"date": "2024-01-12", "category": "Utilities", "amount": 120.00, "description": "Electricity bill"},
    {"date": "2024-01-14", "category": "Food", "amount": 55.20, "description": "Restaurant dinner"},
    {"date": "2024-01-15", "category": "Transport", "amount": 30.00, "description": "Taxi"},
    {"date": "2024-01-17", "category": "Entertainment", "amount": 14.99, "description": "Streaming subscription"},
    {"date": "2024-01-20", "category": "Food", "amount": 38.00, "description": "Groceries"},
    {"date": "2024-01-22", "category": "Utilities", "amount": 45.00, "description": "Internet bill"},
    {"date": "2024-01-25", "category": "Transport", "amount": 22.00, "description": "Train ticket"},
    {"date": "2024-01-28", "category": "Entertainment", "amount": 25.00, "description": "Book"},
]

total = 0
count = 0

for expense in expenses:
    total += expense["amount"]
    count += 1

print(f"Total expenses: {total:.2f}")
print(f"Number of records: {count}")
category_totals = {}

for expense in expenses:
    category = expense["category"]

    if category not in category_totals:
        category_totals[category] = 0

    category_totals[category] += expense["amount"]

print("\nCategory breakdown:")

for category in sorted(category_totals):
    print(f"{category}: {category_totals[category]:.2f}")
    most_expensive = expenses[0]
least_expensive = expenses[0]

for expense in expenses:

    if expense["amount"] > most_expensive["amount"]:
        most_expensive = expense

    if expense["amount"] < least_expensive["amount"]:
        least_expensive = expense

print("\nMost expensive:")
print(f'{most_expensive["description"]} ({most_expensive["category"]}) - {most_expensive["amount"]:.2f}')

print("\nLeast expensive:")
print(f'{least_expensive["description"]} ({least_expensive["category"]}) - {least_expensive["amount"]:.2f}')
average = total / count

print(f"\nAverage expense: {average:.2f}")
print("Expenses above average:")

for expense in expenses:

    if expense["amount"] > average:
        print(f'- {expense["description"]} ({expense["amount"]:.2f})')