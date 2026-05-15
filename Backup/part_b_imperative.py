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

#// B1 - total and count
total = 0
count = 0
for e in expenses:
    total += e["amount"]
    count += 1
print(f"Total expenses: {total:.2f}")
print(f"Number of records: {count}")

#// B2 - category breakdown
cat_totals = {}
for e in expenses:
    cat = e["category"]
    amt = e["amount"]
    if cat in cat_totals:
        cat_totals[cat] += amt
    else:
        cat_totals[cat] = amt
print("\nCategory breakdown:")
for cat in sorted(cat_totals.keys()):
    print(f"  {cat:15} : {cat_totals[cat]:.2f}")


# B3 - most and least expensive (no max/min)
max_expense = expenses[0]
min_expense = expenses[0]
for e in expenses:
    if e["amount"] > max_expense["amount"]:
        max_expense = e
    if e["amount"] < min_expense["amount"]:
        min_expense = e
print(f"\nMost expensive : {max_expense['description']} ({max_expense['category']}) — {max_expense['amount']:.2f}")
print(f"Least expensive: {min_expense['description']} ({min_expense['category']}) — {min_expense['amount']:.2f}")
# B4 - expenses above average
sum_avg = 0
cnt_avg = 0
for e in expenses:
    sum_avg += e["amount"]
    cnt_avg += 1
average = sum_avg / cnt_avg

above = []
for e in expenses:
    if e["amount"] > average:
        above.append(f"{e['description']} ({e['amount']:.2f})")

print(f"\nAverage expense: {average:.2f}")
print("Expenses above average:")
for item in above:
    print(f"  - {item}")