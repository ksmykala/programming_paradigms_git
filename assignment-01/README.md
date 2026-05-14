# expense tracker - assignment 01

## what the project does

this is an expense tracker that goes through a list of 12 expenses and answers some basic questions about them. the expenses have a date, category, amount and description. the same problems are solved three different times using three different paradigms (imperative, procedural and functional) so you can see how the code changes depending on the style you pick.

the tracker answers these questions:

- what is the total amount spent and how many records are there
- how much was spent in each category
- what is the most expensive expense and what is the least expensive
- which expenses are above the average

## how to run

go into the assignment-01 folder and run each file with python:

```bash
python part_b_imperative.py
python part_c_procedural.py
python part_d_functional.py
```

part a is just a markdown file with my paradigm explanations, you do not run it.

sample output when you run part b or part c:

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

what made it easy is that imperative code is basically how i think when i am solving a problem. you start with a variable at zero, you loop through the data, you add to the variable. it is very direct and you can see what is happening at every step.

what made it hard is that there is a lot of repetition. for almost every question i had to write a new loop with new variables, and some of the loops looked almost the same. if i forgot to reset a variable somewhere there would be a bug that is hard to find.

if the dataset grew to 100 000 records the code would still work because python can loop through that many items no problem. the bigger issue is that the file would be very long and messy because everything is written out from scratch. it would be readable for small problems but not for big ones.

### procedural (part c)

what made it easy is that once you have a function like get_total or get_average you can just call it whenever you need it. print_summary becomes very short because it just calls the other functions in order. it also makes the code easier to read because each function does one thing and you can give it a clear name.

what made it hard is deciding what each function should do. some functions ended up needing other functions inside them (like get_average uses get_total and get_count) and you have to be careful not to make functions that do too much.

if the dataset grew to 100 000 records the procedural code would handle it well. the functions stay the same, only the data gets bigger. it is also much more readable because you can understand what the code does just by reading the function names without going into the details.

### functional (part d)

what made it easy is that some problems became one line. get_total_functional is just sum of a generator expression, that is it. map and filter with lambdas are also very short and you can read them like a sentence (filter the expenses where amount is bigger than average).

what made it hard is that get_category_totals_functional took me a while to figure out because python does not have a built in groupby function. i had to first get the unique categories using a set, then for each category sum up the matching expenses. it works but it loops through the data multiple times.

if the dataset grew to 100 000 records the functional code would still work and would actually use less memory because generators do not build the full list in memory at once. the only problem is the category totals function because it goes through the whole list once per category. for 100 000 records with only 4 categories that is 400 000 operations which is fine, but it is not the most efficient way.

## one thing i would do differently

if i had to start over i would use f-strings from the beginning for printing. right now i am using print with commas which adds extra spaces and rounds floats in a weird way (like 67.0 instead of 67.00). f-strings would let me control the spacing and the decimal places exactly, and the output would look closer to what the assignment expected. it is a small thing but it would make the output look more professional.

## file structure

```
assignment-01/
├── README.md
├── part_a_paradigms.md
├── part_b_imperative.py
├── part_c_procedural.py
└── part_d_functional.py
```
