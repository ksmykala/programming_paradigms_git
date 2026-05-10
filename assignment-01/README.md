# Expense Tracker Project

1. Project Overview
The **Expense Tracker** is a Python-based data processing application designed to manage and analyze personal financial records. Each record consists of a date, an amount, a category, and a description, structured as a list of dictionaries. 

The project demonstrates how to handle this dataset and perform common analytical tasks such as calculating totals, finding averages, identifying the most expensive items, and generating category-specific breakdowns. It solves the same problem using three distinct programming paradigms to highlight how different approaches handle the exact same logic.

2. How to Run the Project
You can execute each paradigm's script directly from your terminal. Make sure you are in the project directory, then run the following commands:

python part_b_imperative.py
python part_c_procedural.py
python part_d_functional.py

### Sample Output
Running any of the scripts will produce a formatted summary report similar to this:
"""
Total expenses: 476.44
Number of records: 12

Category breakdown:
  Entertainment : 25.00
  Food          : 216.45
  Transport     : 45.00
  Utilities     : 189.99

Most expensive : Electricity bill (Utilities) — 120.00
Least expensive: Coffee & snack (Food) — 8.75
...

3. Paradigm Comparison
- Imperative (Part B)
    - What made it easy/hard: It felt the most intuitive way to start writting because you tell the program exactly what to do with step-by-step instruction. The syntax isn't difficult to read. However, it quickly became difficult to manage (e.g task B2) since all the logics bundled into one massive block of code, from which finding a specific bug or variable was quite tedious.
    - Scalability: the code would work technically, but it will be time-consuming to read or update. If we add more features for the program and still keep the Imperative Programming style, performance might take a hit.

- Procedural (Part C)
    - What made it easy/hard: this style was easier to test and debug. By breaking the code into smaaller, reusable, single-purpose functions, I could test one specific function at a time. Doing function calls looks more neat and clean (since you only need to remember the function's name). If anyone wants to check any specific function's logic, they can dig further into its function's body. The hard part was making sure the data was passed correctly.
    -  Scalability: highly readable and maintainable at scale. I prefer this style to lengthy imperative style.

- Functional Style (Part D)
    - What made it easy/hard: this was the hardest to understand, but the cleanest to look at once finished. Using map, filter, and comprehensions requires shifting from telling the computer how to loop, to telling it what the result should be.
    - Scalability: Python's generator expressions (like the ones used inside sum()) are incredibly memory-efficient because they don't create massive lists in memory. However, nested comprehensions (like checking every category against the entire list) could result in scanning the 100,000 records repeatedly, which would cause significant processing delays.

4. Future Improvement
- If I had to start this project over from scratch, I would build **Input Validation** first. Currenly, there is no function to check whether a user typed in corrected data or not. 
- If a user types in "-25.00" as one spending instead of 25.00(as the format the program expects), the current will still accept that data and produce the incorrect total sum for example. 
- It can also be the mismatch date type. The program expects format of YYYY-MM-DD and if users aren't aware, they can try to put in 2 Sep 2024 for example, which can crash the program.

- Another improvement could be the cleaning up feature so users can start enter their spending for the new month(s).