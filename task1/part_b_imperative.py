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

# calculating total and count of expenses
total = 0
count = 0
for e in expenses:
    total += e["amount"]
    count += 1
print(f"Total expenses: {total:.2f}")
print(f"Number of records: {count}")

# splitting it into categories
cat_totals = {}
for e in expenses:
    cat = e["category"]
    if cat not in cat_totals:
        cat_totals[cat] = 0
    cat_totals[cat] += e["amount"]

print("\nCategory breakdown:")
for cat in sorted(cat_totals.keys()):
    print(f"  {cat} : {cat_totals[cat]:.2f}")

# checking minimum and maximum 
max_amount = expenses[0]["amount"]
most = expenses[0]
for e in expenses[1:]:
    if e["amount"] > max_amount:
        max_amount = e["amount"]
        most = e

min_amount = expenses[0]["amount"]
least = expenses[0]
for e in expenses[1:]:
    if e["amount"] < min_amount:
        min_amount = e["amount"]
        least = e

print(f"\nMost expensive : {most['description']} ({most['category']}) — {most['amount']:.2f}")
print(f"Least expensive: {least['description']} ({least['category']}) — {least['amount']:.2f}")

# checking above average expenses using loop
total = 0
count = 0
for e in expenses:
    total += e["amount"]
    count += 1
average = total / count

above = []
for e in expenses:
    if e["amount"] > average:
        above.append(f"  - {e['description']} ({e['amount']:.2f})")

print(f"\nAverage expense: {average:.2f}")
print("Expenses above average:")
for line in above:
    print(line)
