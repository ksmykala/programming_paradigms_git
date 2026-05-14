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

# b1 total and count
total_expenses = 0
total_records = 0
for e in expenses:
    total_expenses += e["amount"]
    total_records += 1

print("total expenses: ", round(total_expenses, 2))
print("number of records: ", total_records)

# b2 category breakdown
category_totals = {}
for e in expenses:
    cat = e["category"]
    if cat in category_totals:
        category_totals[cat] += e["amount"]
    else:
        category_totals[cat] = e["amount"]

# sort categories alphabetically
sorted_cats = []
for cat in category_totals:
    sorted_cats.append(cat)

for i in range(len(sorted_cats)):
    for j in range(i + 1, len(sorted_cats)):
        if sorted_cats[i] > sorted_cats[j]:
            temp = sorted_cats[i]
            sorted_cats[i] = sorted_cats[j]
            sorted_cats[j] = temp

print("\ncategory breakdown:")
for cat in sorted_cats:
    total = category_totals[cat]
    print("  ", cat, ":", round(total, 2))

# b3 most and least expensive
most_expensive = expenses[0]
least_expensive = expenses[0]
for e in expenses:
    if e["amount"] > most_expensive["amount"]:
        most_expensive = e
    if e["amount"] < least_expensive["amount"]:
        least_expensive = e

print("\nmost expensive : ", most_expensive["description"], "(", most_expensive["category"], ") -", round(most_expensive["amount"], 2))
print("least expensive: ", least_expensive["description"], "(", least_expensive["category"], ") -", round(least_expensive["amount"], 2))

# b4 expenses above average
total = 0
count = 0
for e in expenses:
    total += e["amount"]
    count += 1

average = total / count

above_average = []
for e in expenses:
    if e["amount"] > average:
        above_average.append(e)

print("\naverage expense: ", round(average, 2))
print("expenses above average:")
for e in above_average:
    print("  -", e["description"], "(", round(e["amount"], 2), ")")
