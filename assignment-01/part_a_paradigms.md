## Snippet 1
**Paradigm**: imperative

**Explanation**: this is imperative because it shows how to perform the program step by step with a loop and an assignment operator. it starts with total = 0, then goes through each expense one by one and keeps adding to total. the code is basically a list of instructions that change the value of a variable over time.

## Snippet 2
**Paradigm**: procedural

**Explanation**: this is procedural because it groups the code into get_total and get_by_category functions. each function does one specific job and you call them when you need them. instead of writing the same loop over and over, you just call the function with the data you want to work on.

## Snippet 3
**Paradigm**: imperative

**Explanation**: this is imperative because the main part of the code still uses a for loop that goes through each expense and updates the totals dictionary one step at a time. it does have a functional element at the end with the lambda inside max(), but the way the dictionary is built is step by step imperative code, so that is the main paradigm.

## Snippet 4
**Paradigm**: functional

**Explanation**: this is functional because it uses the sum function and passes a generator expression to it, and also uses map and filter with lambdas. there is no for loop and no variable being updated over and over. the code just describes what it wants from the data instead of how to build it step by step.
