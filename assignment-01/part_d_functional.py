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

#---TASK D1---
from part_c_procedural import get_total

def get_total_functional(expense_list):
    """Calculate total using sum() and a generator expression."""
    return sum(expense["amount"] for expense in expense_list)

total_c = get_total(expenses)
total_d = get_total_functional(expenses)

print(f"Part C: {total_c}")
print(f"Part D: {total_d}")
print(f"Match: {total_c == total_d}")

#---TASK D2---
from part_c_procedural import get_category_totals

def get_category_totals_functional(expense_list):
    """
    Build the category → total mapping using a dict comprehension
    and a generator expression (no explicit for-loop).
    """
    # {} set comprehension, a set cannot contain a duplicate
    categories = {expense["category"] for expense in expense_list}
    return {
        # declare the result first
        cat: sum(ex["amount"] for ex in expense_list if ex["category"] == cat)
        # then run the loop to get the final result
        for cat in categories
    }

category_total_c = get_category_totals(expenses)
category_total_d = get_category_totals_functional(expenses)

print(f"Part C: {category_total_c}")
print(f"Part D: {category_total_d}")
print(f"Match: {category_total_c == category_total_d}")

#---TASK D3---
from part_c_procedural import get_above_average

def get_above_average_functional(expense_list):
    """
    Return expenses above the average amount.
    Use filter() and a lambda — no explicit for-loop.
    """
    if not expense_list:
        return []
    
    avg = sum(ex["amount"] for ex in expense_list) / len(expense_list)

    # filter(rule, data)
    filtered_iterator = filter(lambda ex: ex["amount"] > avg, expense_list)

    # filter() returns an "iterator", so it must be converted back into a list
    return list(filtered_iterator)

above_avg_c = get_above_average(expenses)
above_avg_d = get_above_average_functional(expenses)

print(f"Part C: {above_avg_c}")
print(f"Part D: {above_avg_d}")
print(f"Match: {above_avg_c == above_avg_d}")

#---TASK D4---
def format_expenses(expense_list):
    """
    Return a list of strings in the format:
    "YYYY-MM-DD | Category | Description | $amount"
    Use map() and a lambda.
    """
    # map(function, data)
    formatted_iterator = map(
        lambda ex: f"{ex["date"]} | {ex["category"]:15} | {ex["description"]:25} | ${ex["amount"]:.2f}",
        expense_list
    )

    return list(formatted_iterator)

if __name__ == "__main__":
    from part_c_procedural import (
        get_total, get_category_totals, get_above_average
    )

    assert round(get_total_functional(expenses), 2) == round(get_total(expenses), 2), \
        "D1 total mismatch"

    assert get_category_totals_functional(expenses) == get_category_totals(expenses), \
        "D2 category totals mismatch"

    proc_ids  = {id(e) for e in get_above_average(expenses)}
    func_ids  = {id(e) for e in get_above_average_functional(expenses)}
    assert proc_ids == func_ids, "D3 above-average mismatch"

    print("All assertions passed.")
    print("\nFormatted expenses:")
    for line in format_expenses(expenses):
        print(line)