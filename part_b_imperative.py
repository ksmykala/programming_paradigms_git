print("This line will be printed.")
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
