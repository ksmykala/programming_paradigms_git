## Snippet 1
total = 0
for expense in expenses:
    total += expense["amount"]
print(f"Total spending: {total:.2f}")

**Paradigm**: Imperative Programming
**Explanation**: 
- uses step-by-step approach using a loop to update value of mutable variable "total"
- instructs the computer how to update the accumulator by iterating through the "expenses" list and incremeting the value manually

## Snippet 2
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

**Paradigm**: Procedural Programming
**Explanation**: 
- we have reusable functions (get_total and get_by_category) the perform specific tasks
- The functions' body build on imperative method but emphasizes modularity and passing-of-argument into procedures to get a result 

## Snippet 3
totals = {}
for expense in expenses:
    cat = expense["category"]
    totals[cat] = totals.get(cat, 0) + expense["amount"]
most_expensive_category = max(totals, key=lambda cat: totals[cat])


**Paradigm**: Imperative Programming
**Explanation**:
- the main logic is imperative because it has a for loop to calculate the total spending for each catergory
- max() and lambda in the end are functional helper methods (Declarative/ Functional)

## Snippet 4
food_total = sum(
    e["amount"]
    for e in expenses
    if e["category"] == "Food"
)

amounts = list(map(lambda e: e["amount"], expenses))
above_average = list(filter(lambda a: a > sum(amounts) / len(amounts), amounts))

**Paradigm**: Functional Programming
**Explanation**:
- avoids explicit loops and tate mutation by using higher-order functions like map and filter, along with a generator expression.
- focuses on "what" to transform (mapping anf iltering data) rather than "how" to manage the iteration index or temporary counters