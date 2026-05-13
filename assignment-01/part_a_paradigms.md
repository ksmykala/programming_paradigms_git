# Part A — Paradigm Identification

## Snippet 1
**Paradigm**: Imperative

**Explanation**: The code just goes through each expense one by one and adds the amount to total.
The variable total keeps changing every time the loop runs. You are telling the computer exactly what to do step by step.

---

## Snippet 2
**Paradigm**: Procedural

**Explanation**: The code is split into two functions and each function does one job.
Instead of writing everything in one place the code is organized into get_total and get_by_category.
This makes it easier to reuse the code.

---

## Snippet 3
**Paradigm**: Imperative with a Functional touch

**Explanation**: The code uses a loop to go through the expenses and adds amounts into a dictionary. 
At the end it uses a lambda to find the most expensive category which is a small functional touch but the rest is still imperative.

---

## Snippet 4
**Paradigm**: Functional

**Explanation**: This code does not use any regular for loops. It uses map filter and lambda to work with the data.
You just say what you want and the functions figure out how to do it.
