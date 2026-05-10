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
    Calculate the total amount of all expenses.

    Parameters:
        expense_list (list): List of expense dictionaries.

    Returns:
        float: Sum of all 'amount' values.
    """
    total_sum = 0.0

    for exepense in expense_list:
        total_sum += exepense["amount"]

    return total_sum  

def get_count(expense_list):
    """Return the number of expense records."""
    record_count = 0

    for expense in expense_list:
        record_count += 1
    return record_count

def get_category_totals(expense_list):
    """
    Build a mapping from category names to their total amounts.

    Returns:
        dict: {category: total_amount}
    """
    category_total = {}
    for expense in expense_list:
        category = expense["category"]
        amount = expense ["amount"]

        # Check if the category is already in category_total
        if category in category_total:
            category_total[category] += amount
        else:
            # Create a new entry for this category
            category_total[category] = amount

    return category_total

def get_most_expensive(expense_list):
    """Return the expense dict with the highest amount (no max() built-in)."""

    if not expense_list:
        return None
    
    # Set the first item of the list is the most expensive
    most_expensive = expense_list[0]

    # Starting checking with each subsequent item in the list and update the most expensive if it matches the condition
    for expense in expense_list:
        if expense["amount"] > most_expensive["amount"]:
            most_expensive = expense

    return most_expensive


def get_least_expensive(expense_list):
    """Return the expense dict with the lowest amount (no min() built-in)."""

    if not expense_list:
        return None
    
    # Set the first item of the list is the most expensive
    least_expensive = expense_list[0]

    # Starting checking with each subsequent item in the list and update the most expensive if it matches the condition
    for expense in expense_list:
        if expense["amount"] < least_expensive["amount"]:
            least_expensive = expense

    return least_expensive

def get_average(expense_list):
    """Return the average expense amount as a float."""
    total_sum = 0.0
    count = 0

    for expense in expense_list:
        total_sum += expense["amount"]
        count += 1

    average_expense = total_sum / count
    return average_expense


def get_above_average(expense_list):
    """
    Return a list of expense dicts whose amount is strictly above the average.
    """
    total_sum = 0.0
    count = 0
    for expense in expense_list:
        total_sum += expense["amount"]
        count += 1
    
    # Handle the case where the list might be empty to avoid division by zero
    if count == 0:
        return []
        
    avg = total_sum / count
    
    # Make the list
    above_average = []
    for expense in expense_list:
        if expense["amount"] > avg:
            above_average.append(expense)
            
    return above_average


def print_summary(expense_list):
    """
    Print a full summary report using the helper functions above.
    Produce the same output as Parts B1–B4 combined.
    """
    # Task B1: Total and Count
    total = get_total(expense_list)
    count = get_count(expense_list)
    print(f"Total expense: {total:.2f}")
    print(f"Number of records: {count}")
    print()

    # Task B2: Category Breakdown
    print("Category breakdown:")
    cat_totals = get_category_totals(expense_list)

    # Sorting alphabetically
    categories = []
    for cat in cat_totals:
        categories.append(cat)
    
    # Manual Bubble Sort for alphabetical order
    n = len(categories)
    for i in range(n):
        for j in range(0, n - i - 1):
            if categories[j] > categories[j + 1]:
                temp = categories[j]
                categories[j] = categories[j + 1]
                categories[j + 1] = temp
                
    for cat in categories:
        print(f"  {cat:13} : {cat_totals[cat]:.2f}")
    print()

    # Task B3: Most and Least Expensive
    most = get_most_expensive(expense_list)
    least=get_least_expensive(expense_list)

    print(f"Most expensive: {most["description"]} ({most["category"]}) - {most["amount"]:.2f}")
    print(f"Least expensive: {least["description"]} ({least["category"]}) - {least["amount"]:.2f}")
    print()

    # Task B4: Above Average
    avg = get_average(expense_list)
    print(f"Average expense: {avg:.2f}")
    print("Expenses above average:")
    above_avg = get_above_average(expense_list)
    for item in above_avg:
        print(f"  - {item["description"]} ({item["amount"]:.2f})")

if __name__ == "__main__":   
    print_summary(expenses)