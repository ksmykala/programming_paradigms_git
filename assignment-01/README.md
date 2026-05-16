# assignment 01

## what the project does

this is an expense tracker that goes through a list of 12 expenses and answers some basic questions. the same problems are solved three different times in three different paradigms (imperative, procedural, functional) so you can see how the code changes depending on the style.

the tracker answers:

- what is the total spent and how many records are there
- how much was spent in each category
- what is the most and least expensive expense
- which expenses are above the average

## how to run

go into the assignment-01 folder and run each file with python:

```bash
python part_b_imperative.py
python part_c_procedural.py
python part_d_functional.py
```

part a is just a markdown file, you do not run it.

sample output:

```
total expenses:  476.44
number of records:  12

category breakdown:
   Entertainment : 99.99
   Food : 144.45
   Transport : 67.0
   Utilities : 165.0

most expensive :  Electricity bill ( Utilities ) - 120.0
least expensive:  Coffee & snack ( Food ) - 8.75

average expense:  39.7
expenses above average:
  - Groceries ( 42.5 )
  - Concert ticket ( 60.0 )
  - Electricity bill ( 120.0 )
  - Restaurant dinner ( 55.2 )
  - Internet bill ( 45.0 )
```

## paradigm comparison

### imperative (part b)

easy because imperative code is how i think when solving a problem. you start with a variable at zero, loop through the data, add to it. very direct.

hard because there is a lot of repetition. almost every question needed a new loop with new variables and they looked almost the same. easy to forget to reset a variable somewhere.

at 100 000 records the code would still work but the file would be very long and messy. readable for small problems, not for big ones.

### procedural (part c)

easy because once you have a function like get_total you just call it whenever you need it. print_summary is short because it just calls the other functions.

hard because deciding what each function should do takes thought. some functions ended up using other functions (get_average uses get_total and get_count).

at 100 000 records this handles it well. functions stay the same, only the data gets bigger. also more readable because the function names tell you what is happening.

### functional (part d)

easy because some problems become one line. get_total_functional is just sum of a generator. map and filter with lambdas read like a sentence.

hard because get_category_totals_functional took a while to figure out since python has no built in groupby. i had to first get unique categories using a set, then sum up matching expenses for each one.

at 100 000 records it would still work and use less memory because generators do not build the full list at once. only problem is category totals loops through the data once per category, but with only 4 categories it is fine.

## one thing i would do differently

if i had to start over i would not write a full bubble sort for sorting just 4 categories. the assignment said no sorted() builtin so i reached for bubble sort because that is what i remembered from class, but for only 4 items the temp variable and nested loops are way more code than needed. it is also very slow. i could have just written the categories in alphabetical order by hand.

i would also handle edge cases better. for example get_most_expensive starts with expense_list[0] which would crash on an empty list. it does not matter for this assignment because the dataset always has 12 expenses, but real code should not assume the input is always clean.
