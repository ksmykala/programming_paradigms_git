# Personal Expense Tracker

## Project Description

This project is a Personal Expense Tracker developed in Python. The program reads a dataset of expenses and calculates useful statistics such as total spending, category totals, most expensive expense, least expensive expense, and expenses above the average amount.

The assignment was implemented using three different programming paradigms:

- Imperative Programming
- Procedural Programming
- Functional Programming

This allows comparison between different approaches to solving the same problem.

## How to Run

Run the files from the command line:

```bash
python part_b_imperative.py
python part_c_procedural.py
python part_d_functional.py
```

## Paradigm Comparison

### Imperative Programming

The imperative version was straightforward to write because it uses loops, variables, and conditionals. However, the code becomes longer and harder to maintain as the project grows.

If the dataset increased to 100,000 records, the program would still work, but the code could become difficult to manage because all logic is contained in a single block.

### Procedural Programming

The procedural version improves organization by dividing the logic into functions. Each function has a single responsibility, making the code easier to read, test, and maintain.

With 100,000 records, the program would still work well and remain readable because the logic is separated into reusable functions.

### Functional Programming

The functional version uses tools such as map(), filter(), lambda expressions, and comprehensions. This often results in shorter and more expressive code.

With a larger dataset, the code would still work efficiently. However, excessive use of functional constructs can sometimes reduce readability for beginners.

## What I Would Do Differently

If I started over, I would create reusable helper functions earlier and improve the report formatting. I would also add support for reading expense data from external files instead of storing the dataset directly in the source code.

## Sample Output

```text
Total expenses: 476.44
Number of records: 12

Category breakdown:
Entertainment : 99.99
Food : 144.45
Transport : 67.00
Utilities : 165.00
```