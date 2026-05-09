print("This line will be printed.")
# Part D — Functional Elements (20 points)
# File: part_d_functional.py
#
# Rewrite four of the functions from Part C using functional-style tools (map, filter, lambda, list/generator comprehensions). Import your Part C functions and compare the results — both versions must give the same answer.
#
# D1 — Total with sum + generator expression (4 pts)
# def get_total_functional(expense_list):
#     """Calculate total using sum() and a generator expression."""
#     pass
# D2 — Category totals with a dict comprehension (6 pts)
# def get_category_totals_functional(expense_list):
#     """
#     Build the category → total mapping using a dict comprehension
#     and a generator expression (no explicit for-loop).
#     """
#     pass
# Hint: collect unique categories first, then map each category to its total.
#
# D3 — Above-average expenses with filter + lambda (5 pts)
# def get_above_average_functional(expense_list):
#     """
#     Return expenses above the average amount.
#     Use filter() and a lambda — no explicit for-loop.
#     """
#     pass
# D4 — Formatted descriptions with map + lambda (5 pts)
# def format_expenses(expense_list):
#     """
#     Return a list of strings in the format:
#     "YYYY-MM-DD | Category | Description | $amount"
#     Use map() and a lambda.
#     """
#     pass
# Expected output for format_expenses (first two lines):
#
# 2024-01-05 | Food          | Groceries        | $42.50
# 2024-01-07 | Transport     | Bus pass         | $15.00
# (Spacing does not need to be exact.)
#
# Verification block — include this at the bottom of part_d_functional.py:
#
# if __name__ == "__main__":
#     from part_c_procedural import (
#         get_total, get_category_totals, get_above_average
#     )
#
#     assert round(get_total_functional(expenses), 2) == round(get_total(expenses), 2), \
#         "D1 total mismatch"
#
#     assert get_category_totals_functional(expenses) == get_category_totals(expenses), \
#         "D2 category totals mismatch"
#
#     proc_ids  = {id(e) for e in get_above_average(expenses)}
#     func_ids  = {id(e) for e in get_above_average_functional(expenses)}
#     assert proc_ids == func_ids, "D3 above-average mismatch"
#
#     print("All assertions passed.")
#     print("\nFormatted expenses:")
#     for line in format_expenses(expenses):
#         print(line)
