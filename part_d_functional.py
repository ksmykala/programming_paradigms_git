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
#D1
def get_total_functional(expense_list):
    return sum(exp["amount"] for exp in expense_list)

#D2
def get_category_totals_functional(expense_list):
    unique_categories = {exp["category"] for exp in expense_list}
    return {
        cat: sum(exp["amount"] for exp in expense_list if exp["category"] == cat)
        for cat in unique_categories
    }

#D3
def get_above_average_functional(expense_list):
    total = sum(exp["amount"] for exp in expense_list)
    avg = total / len(expense_list)
    return list(filter(lambda exp: exp["amount"] > avg, expense_list))

#D4
def format_expenses(expense_list):
    return list(
        map(
            lambda e: f"{e['date']} | {e['category']:<14} | {e['description']:<16} | ${e['amount']:}",
            expense_list,
        )
    )

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