print("This line will be printed.")

# Dataset
# All parts of this assignment work with the following dataset. Copy it into each of your Python files:
#
# expenses = [
#     {"date": "2024-01-05", "category": "Food",          "amount": 42.50, "description": "Groceries"},
#     {"date": "2024-01-07", "category": "Transport",     "amount": 15.00, "description": "Bus pass"},
#     {"date": "2024-01-09", "category": "Entertainment", "amount": 60.00, "description": "Concert ticket"},
#     {"date": "2024-01-10", "category": "Food",          "amount": 8.75,  "description": "Coffee & snack"},
#     {"date": "2024-01-12", "category": "Utilities",     "amount": 120.00,"description": "Electricity bill"},
#     {"date": "2024-01-14", "category": "Food",          "amount": 55.20, "description": "Restaurant dinner"},
#     {"date": "2024-01-15", "category": "Transport",     "amount": 30.00, "description": "Taxi"},
#     {"date": "2024-01-17", "category": "Entertainment", "amount": 14.99, "description": "Streaming subscription"},
#     {"date": "2024-01-20", "category": "Food",          "amount": 38.00, "description": "Groceries"},
#     {"date": "2024-01-22", "category": "Utilities",     "amount": 45.00, "description": "Internet bill"},
#     {"date": "2024-01-25", "category": "Transport",     "amount": 22.00, "description": "Train ticket"},
#     {"date": "2024-01-28", "category": "Entertainment", "amount": 25.00, "description": "Book"},
# ]


# Part B — Imperative Implementation (25 points)
# File: part_b_imperative.py
#
# Using only variables, loops (for/while), conditionals (if/elif/else), and accumulator variables — no helper functions, no map/filter/sum/max builtins — implement the following:
#
# B1 — Total and count (5 pts)
# Compute and print:
#
# the total amount spent across all expenses
# the number of expenses recorded
# Expected output:
#
# Total expenses: 476.44
# Number of records: 12
# B2 — Category breakdown (8 pts)
# Build a dictionary that maps each category name to the total amount spent in that category. Print each entry sorted alphabetically by category name.
#
# Expected output:
#
# Category breakdown:
#   Entertainment : 99.99
#   Food          : 144.45
#   Transport     : 67.00
#   Utilities     : 165.00
# (Amounts must be formatted to 2 decimal places. Spacing does not need to be exact.)
#
# B3 — Most and least expensive (7 pts)
# Find and print the single most expensive and single least expensive expense record.
# Do not use the built-in max() or min() functions — implement the search with a loop and a tracking variable.
#
# Expected output:
#
# Most expensive : Electricity bill (Utilities) — 120.00
# Least expensive: Coffee & snack (Food) — 8.75
# B4 — Expenses above average (5 pts)
# First compute the average expense amount using a loop. Then, using a second loop, collect all expense descriptions whose amount is strictly above the average. Print them.
#
# Expected output:
#
# Average expense: 39.70
# Expenses above average:
#   - Concert ticket (60.00)
#   - Electricity bill (120.00)
#   - Restaurant dinner (55.20)
#   - Internet bill (45.00)
