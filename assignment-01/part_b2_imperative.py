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

#---TASK B2---
# An empty dictionary to store totals for each category
category_totals = {}

for expense in expenses:
    category = expense["category"]
    amount = expense["amount"]

    # Check if the category is already in category_totals 
    if category in category_totals:
        category_totals[category] += amount
    # If not then create a new category with the current amount
    else:
        category_totals[category] = amount
    
# To print alphabetically, first extract the keys (category names)
categories = []
for cat in category_totals:
    categories.append(cat)              # add each category's name to the back of the list

n = len(categories)
for i in range(n):                      # n = 4, range(4) = 0,1,2,3
    for j in range(0, n - i - 1):       
        # -1: avoid index-of-range error, categories[3] compares to categories[4] while there is no such categories[4]
        # -i: reduce the checked loop
        if categories[j] > categories[j + 1]:
            # Swap elements if they are in the wrong order
            temp = categories[j]
            categories[j] = categories[j + 1]
            categories[j + 1] = temp

print("Category breakdown")
for cat in categories:
    total = category_totals[cat]

    # {cat:13} reserves 13 characters of space for this string, make them aligned when printing out
    print(f"  {cat:13} : {total:.2f}")
