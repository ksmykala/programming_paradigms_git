Note to self
Reminders about git
You have an alias: git config --global alias.acp '!f() { git add -A && git commit -m "$1" && git push; }; f'
You just have to: git acp "message"
TASK STUFF

Part E — README (10 points)
File: README.md

Write a Markdown document (minimum 300 words) that covers:

What the project does — briefly describe the Expense Tracker.
How to run it — commands to execute each part (e.g. python part_b_imperative.py).
Paradigm comparison — for each of the three styles (imperative, procedural, functional), explain:
What made it easy or hard to write that way?
What would happen if the dataset grew to 100 000 records — would your code still work? Would it be readable?
One thing you would do differently if you had to start over.
Use proper Markdown: at least one heading level, a code block showing a sample run, and a bulleted or numbered list.



Repository Structure
Submit your work as a GitHub repository with the following layout:

assignment-01/
├── README.md
├── part_a_paradigms.md
├── part_b_imperative.py
├── part_c_procedural.py
└── part_d_functional.py
All Python files must be runnable from the command line without errors (python <file>.py).

Submission instructions
Create a folder called assignment-01 in GitHub repository (the one you were given access to in class [use your own branch], or your own public repo).
Push all five files listed above.
Submit the link on Moodle.
Note: commit messages matter — use clear, descriptive messages (e.g. Add Part B imperative implementation). A repo with a single "upload all files" commit will lose 2 points.


Grading Rubric
Part	Max pts	Key criteria
A — Paradigm Identification	10	Correct identification + clear explanation for each snippet
B — Imperative	25	Correct outputs; no helper functions; no map/filter/sum/max/min builtins
C — Procedural	35	All functions present; docstrings; print_summary delegates to helpers; same output as B
D — Functional	20	Correct functional rewrites; assertions pass; no explicit loops in D1–D4
E — README	10	≥300 words; covers all four required points; proper Markdown
Commit quality	−2	Deducted for a single "dump all" commit

Academic Integrity
You are encouraged to discuss ideas with classmates, but the code and write-up you submit must be your own. Do not copy code from the internet or from other students. Plagiarism will result in a grade of 0 for the assignment. The goal is to fully understand the topic, not to pass the assignment.


Tips
Start with Part B. Once your loops work, refactoring into functions (Part C) is straightforward.
Test each function individually before wiring everything together in print_summary.
Part D: if you are stuck on the dict comprehension in D2, first solve it with a regular loop, then convert it step by step.
README: write it last, after you have seen all three styles side by side — you will have more to say.
Good luck!

