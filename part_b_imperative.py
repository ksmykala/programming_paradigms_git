
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
# B1 - Total and count

# total_expenses = 0
# expense_count = 0
# for expense in expenses:
#     expense_count += 1
#     total_expenses += expense["amount"]
# print("Total expenses: ", total_expenses)
# print(expense_count)

# B2 - category breakdown

# ent_expenses = 0
# food_expenses = 0
# trans_expenses = 0
# util_expenses = 0
# for expense in expenses:
#     if expense["category"] == "Entertainment":
#         ent_expenses += expense["amount"]
#     if expense["category"] == "Transport":
#         trans_expenses += expense["amount"]
#     if expense["category"] == "Utilities":
#         util_expenses += expense["amount"]
#     if expense["category"] == "Food":
#         food_expenses += expense["amount"]
# print("Category breakdown:")
# print("Entertainment:", ent_expenses)
# print("Food:", food_expenses)
# print("Transport:", trans_expenses)
# print("Utilities:", util_expenses)

# B3 - Most and least expensive

# most_expensive_name = " "
# least_expensive_name = " "
# most_expensive = 0
# least_expensive = 1000
# for expense in expenses:
#     if expense["amount"] > most_expensive:
#         most_expensive = expense["amount"]
#         most_expensive_name = expense["description"]
#     if expense["amount"] < least_expensive:
#         least_expensive = expense["amount"]
#         least_expensive_name = expense["description"]
# print("Most expensive " + most_expensive_name + " - ", end = "")
# print(most_expensive)
# print("Least expensive" + least_expensive_name + " - ", end = "")
# print(least_expensive)

# B4 - Expenses above average

# expense_total = 0
#
# expense_count = 0
# for expense in expenses:
#     expense_total += expense["amount"]
#     expense_count += 1
#
# expense_av = expense_total / expense_count
# print(f"Average expense: {expense_av:.2f}")
# print("Expenses above average:")
# for expense in expenses:
#     if expense["amount"] > expense_av:
#         print("- " + expense["description"] + " ", end = " ")
#         print(expense["amount"])
