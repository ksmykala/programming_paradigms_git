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


def get_total(expense_list):
    """
    calculate the total amount of all expenses.

    parameters:
        expense_list (list): list of expense dictionaries.

    returns:
        float: sum of all amount values.
    """
    total = 0
    for e in expense_list:
        total += e["amount"]
    return total


def get_count(expense_list):
    """
    return the number of expense records.

    parameters:
        expense_list (list): list of expense dictionaries.

    returns:
        int: how many records are in the list.
    """
    count = 0
    for e in expense_list:
        count += 1
    return count


def get_category_totals(expense_list):
    """
    build a mapping from category names to their total amounts.

    parameters:
        expense_list (list): list of expense dictionaries.

    returns:
        dict: {category: total_amount}
    """
    totals = {}
    for e in expense_list:
        cat = e["category"]
        if cat in totals:
            totals[cat] += e["amount"]
        else:
            totals[cat] = e["amount"]
    return totals


def get_most_expensive(expense_list):
    """
    return the expense dict with the highest amount (no max built-in).

    parameters:
        expense_list (list): list of expense dictionaries.

    returns:
        dict: the expense record with the biggest amount.
    """
    most_expensive = expense_list[0]
    for e in expense_list:
        if e["amount"] > most_expensive["amount"]:
            most_expensive = e
    return most_expensive


def get_least_expensive(expense_list):
    """
    return the expense dict with the lowest amount (no min built-in).

    parameters:
        expense_list (list): list of expense dictionaries.

    returns:
        dict: the expense record with the smallest amount.
    """
    least_expensive = expense_list[0]
    for e in expense_list:
        if e["amount"] < least_expensive["amount"]:
            least_expensive = e
    return least_expensive


def get_average(expense_list):
    """
    return the average expense amount as a float.

    parameters:
        expense_list (list): list of expense dictionaries.

    returns:
        float: the average of all amount values.
    """
    total = get_total(expense_list)
    count = get_count(expense_list)
    average = total / count
    return average


def get_above_average(expense_list):
    """
    return a list of expense dicts whose amount is strictly above the average.

    parameters:
        expense_list (list): list of expense dictionaries.

    returns:
        list: expenses whose amount is bigger than the average.
    """
    average = get_average(expense_list)
    above_average = []
    for e in expense_list:
        if e["amount"] > average:
            above_average.append(e)
    return above_average


def sort_categories(category_totals):
    """
    return category names sorted alphabetically.

    parameters:
        category_totals (dict): mapping of category to total amount.

    returns:
        list: category names in alphabetical order.
    """
    sorted_cats = []
    for cat in category_totals:
        sorted_cats.append(cat)

    for i in range(len(sorted_cats)):
        for j in range(i + 1, len(sorted_cats)):
            if sorted_cats[i] > sorted_cats[j]:
                temp = sorted_cats[i]
                sorted_cats[i] = sorted_cats[j]
                sorted_cats[j] = temp
    return sorted_cats


def print_summary(expense_list):
    """
    print a full summary report using the helper functions above.
    produces the same output as parts b1 to b4 combined.

    parameters:
        expense_list (list): list of expense dictionaries.

    returns:
        nothing.
    """
    # b1
    total_expenses = get_total(expense_list)
    total_records = get_count(expense_list)
    print("total expenses: ", round(total_expenses, 2))
    print("number of records: ", total_records)

    # b2
    category_totals = get_category_totals(expense_list)
    sorted_cats = sort_categories(category_totals)
    print("\ncategory breakdown:")
    for cat in sorted_cats:
        print("  ", cat, ":", round(category_totals[cat], 2))

    # b3
    most_expensive = get_most_expensive(expense_list)
    least_expensive = get_least_expensive(expense_list)
    print("\nmost expensive : ", most_expensive["description"], "(", most_expensive["category"], ") -", round(most_expensive["amount"], 2))
    print("least expensive: ", least_expensive["description"], "(", least_expensive["category"], ") -", round(least_expensive["amount"], 2))

    # b4
    average = get_average(expense_list)
    above_average = get_above_average(expense_list)
    print("\naverage expense: ", round(average, 2))
    print("expenses above average:")
    for e in above_average:
        print("  -", e["description"], "(", round(e["amount"], 2), ")")


# entry point
if __name__ == "__main__":
    print_summary(expenses)
