Part A — Paradigm Identification (10 points)
File: part_a_paradigms.md

Read the four code snippets below. For each one:

Name the primary programming paradigm being used.
Write 2–3 sentences explaining the specific features of the snippet that indicate that paradigm.
Snippet 1
total = 0
for expense in expenses:
    total += expense["amount"]
print(f"Total spending: {total:.2f}")
Snippet 2
def get_total(expense_list):
    total = 0
    for e in expense_list:
        total += e["amount"]
    return total

def get_by_category(expense_list, category):
    result = []
    for e in expense_list:
        if e["category"] == category:
            result.append(e)
    return result

total = get_total(expenses)
food = get_by_category(expenses, "Food")
Snippet 3
totals = {}
for expense in expenses:
    cat = expense["category"]
    totals[cat] = totals.get(cat, 0) + expense["amount"]
most_expensive_category = max(totals, key=lambda cat: totals[cat])
Snippet 4
food_total = sum(
    e["amount"]
    for e in expenses
    if e["category"] == "Food"
)

amounts = list(map(lambda e: e["amount"], expenses))
above_average = list(filter(lambda a: a > sum(amounts) / len(amounts), amounts))
Answer format — create part_a_paradigms.md with this structure:

## Snippet 1
**Paradigm**: ...
**Explanation**: ...

## Snippet 2
**Paradigm**: ...
**Explanation**: ...

## Snippet 3
**Paradigm**: ...
**Explanation**: ...

## Snippet 4
**Paradigm**: ...
**Explanation**: ...
