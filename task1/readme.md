# Task 1 – Expense Tracker (Three Ways)

## What is this project?

This is a small **Expense Tracker** that reads a list of expenses and prints a summary.  
The summary shows:

- Total money spent
- Number of items bought
- How much I spent in each category (Food, Transport, Entertainment, Utilities)
- The most and least expensive things
- The average expense
- All the items that cost more than the average

The cool part: I wrote the same program **three different ways**:

- once in an *imperative* style
- once in a *procedural* style
- once in a *functional* style. 

There’s also a file called `part_a_paradigms.md` where I classify some code snippets by paradigm type.

The point of the task was to check what is easy to do in each of the styles and what's hard, while also checking how they work.
---

## How to run it

All you need is Python without extra libraries.

```bash
# 1. Download the code
git clone https://github.com/ksmykala/programming_paradigms_git.git
cd programming_paradigms_git

# 2. Switch to my branch (where the actual work lives)
git checkout lab_schmidt
cd task1

# 3. Run each part
python part_b_imperative.py
python part_c_procedural.py
python part_d_functional.py
```

# Example of what's in the files:

Total expenses: 476.44
Number of records: 12

## Category breakdown:
Entertainment : 99.99
Food : 144.45
Transport : 67.00
Utilities : 165.00

Most expensive : Electricity bill (Utilities) — 120.00
Least expensive: Coffee & snack (Food) — 8.75

Average expense: 39.70

## Expenses above average:
- Groceries (42.50)
- Concert ticket (60.00)
- Restaurant dinner (55.20)
- Electricity bill (120.00)
- Internet bill (45.00)

# Paradigm comparsion
## Imperative
- Easy to write by explainin what to do 1:1
- After many runs it still works but finding whats wrong might be challenging

## Procedural
- It's hard to track what the functions take and give out
- After many attempts it would still work but it would be easier to just use a loop

## Functional
- Uses functions to keep the code simpler and cleaner
- Some loops break that cycle like my total accumulator
- Scales good enough but needs to be carefully made

# Things to do differently
- The only thing I would do differently is put the data into a single file and read it from my code instead of pasting it every time
