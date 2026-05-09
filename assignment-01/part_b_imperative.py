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

# B1 — Total and count

expenses_total= 0
record_amount = 0
for expense in expenses:
    expenses_total += expense["amount"]
    record_amount+=1
print(f"Total expenses: {expenses_total:.2f}")
print(f"Number of records: {record_amount}")

# B2 — Category breakdown

category_totals = {}
for i in range(len(expenses)):
    cat = expenses[i]["category"]
    amt = expenses[i]["amount"]

    if cat in category_totals:
        category_totals[cat] = category_totals[cat] + amt
    else:
        category_totals[cat] = amt

print("\nCategory breakdown:")

categories = list(category_totals.keys())
categories.sort()
for i in range(len(categories)):
    cat = categories[i]
    print(" ", cat, ":", format(category_totals[cat], ".2f"))

# B3 — Most and least expensive

max_item = expenses[0]
min_item = expenses[0]
for i in range(1, len(expenses)):
    current = expenses[i]

    if current["amount"] > max_item["amount"]:
        max_item = current

    if current["amount"] < min_item["amount"]:
        min_item = current

print("\nMost expensive :", max_item["description"], "(",max_item["category"],") —", format(max_item["amount"],".2f"))

print("Least expensive:", min_item["description"],"(",min_item["category"],") —", format(min_item["amount"],".2f"))

# B4 — Expenses above average (5 pts)

expenses_total = 0.0
record_amount = 0
#Resetting the values to 0 of expenses_total and record_amount
#So that we can reuse them instead of creating a brand-new variable that does the same thing again
for i in range(len(expenses)):
    expenses_total += expenses[i]["amount"]
    record_amount += 1

average = expenses_total / record_amount

print("\nAverage expense:", format(average, ".2f"))
print("Expenses above average:")

for i in range(len(expenses)):
    if expenses[i]["amount"] > average:
        print("  -", expenses[i]["description"], "(", format(expenses[i]["amount"], ".2f"), ")")
# computed directly from dataset using required logic