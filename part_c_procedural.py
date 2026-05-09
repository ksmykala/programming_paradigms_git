print("This line will be printed.")
# Part C — Procedural Refactoring (35 points)
# File: part_c_procedural.py
#
# Take the logic from Part B and reorganise it into well-named, single-responsibility functions. Each function must have a docstring that describes what it does, its parameters, and its return value. Docstring is already implemented below, but adjust it accordingly.
#
# Implement all of the functions listed below. You may add private helper functions, but the ones listed are mandatory.
#
# def get_total(expense_list):
#     """
#     Calculate the total amount of all expenses.
#
#     Parameters:
#         expense_list (list): List of expense dictionaries.
#
#     Returns:
#         float: Sum of all 'amount' values.
#     """
#     pass
#
#
# def get_count(expense_list):
#     """Return the number of expense records."""
#     pass
#
#
# def get_category_totals(expense_list):
#     """
#     Build a mapping from category names to their total amounts.
#
#     Returns:
#         dict: {category: total_amount}
#     """
#     pass
#
#
# def get_most_expensive(expense_list):
#     """Return the expense dict with the highest amount (no max() built-in)."""
#     pass
#
#
# def get_least_expensive(expense_list):
#     """Return the expense dict with the lowest amount (no min() built-in)."""
#     pass
#
#
# def get_average(expense_list):
#     """Return the average expense amount as a float."""
#     pass
#
#
# def get_above_average(expense_list):
#     """
#     Return a list of expense dicts whose amount is strictly above the average.
#     """
#     pass
#
#
# def print_summary(expense_list):
#     """
#     Print a full summary report using the helper functions above.
#     Produce the same output as Parts B1–B4 combined.
#     """
#     pass
#
#
# # Entry point
# if __name__ == "__main__":
#     print_summary(expenses)
# Requirements checklist for Part C:
#
# [ ] Every function has a docstring.
# [ ] get_most_expensive and get_least_expensive do not use max() / min().
# [ ] print_summary calls the other functions — it does not reimplement logic.
# [ ] Running python part_c_procedural.py produces the same output as Part B.
