# Personal Expense Tracker

## What the project does

This project is a personal expense tracker built in C++. It reads a list of 12 expense records and computes different statistics like total spending, category breakdown, most and least expensive items, and expenses above average. The same logic is implemented in three different programming styles to show the difference between imperative, procedural, and functional programming.

## How to run it

Make sure you have a C++ compiler installed then run these commands:

```
g++ part_b_imperative.cpp -o part_b
./part_b

g++ part_c_procedural.cpp -o part_c
./part_c

g++ part_d_functional.cpp -o part_d
./part_d
```

## Paradigm comparison

### Imperative
- It was easy to write because you just think step by step
- Every loop and every variable is written manually
- If the dataset grew to 100000 records the code would still work but it would be very hard to read because everything is in one big block
- If I started over I would avoid repeating the same loops multiple times

### Procedural
- It was a bit harder to write because you have to think about how to split the logic into functions
- Each function does one job which makes it much easier to read and fix
- With 100000 records it would still work fine and the code would still be clean and readable
- If I started over I would make the functions return values instead of printing directly

### Functional
- It was the hardest to write because the syntax is different and you have to think differently
- Instead of writing loops you use tools like accumulate, copy_if, and transform with lambdas
- With 100000 records it would still work and the code is very short and clean
- If I started over I would learn more about lambdas before starting this part

## Sample output

```
Total expenses: 476.44
Number of records: 12

Category breakdown:
  Entertainment : 99.99
  Food : 144.45
  Transport : 67.00
  Utilities : 165.00

Most expensive : Electricity bill (Utilities) - 120.00
Least expensive: Coffee & snack (Food) - 8.75

Average expense: 39.70
Expenses above average:
  - Concert ticket (60.00)
  - Electricity bill (120.00)
  - Restaurant dinner (55.20)
  - Internet bill (45.00)
```
