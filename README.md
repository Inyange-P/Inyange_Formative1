# Student Grade / Assignment Tracker

**Name:** Inyange Providence
**Course:** Programming One 
**Assignment:** Formative 1
**GitHub repo:** https://github.com/Inyange-P/Inyange_Formative1.git

## What this is

A command-line program to track homework and exam grades. You can add assignments, list them, filter them, and see a summary of your grades. Everything stays in memory while the program runs, no saving to a file, since that's what the assignment asked for.

## Features

- Add homework or exams (subject, title, max score, your score, due date).
- List everything you've added.
- Filter by subject, type (homework/exam), or month.
- Summary: overall average, average per subject, highest and lowest scoring assignment.
- Doesn't crash on bad input. Wrong score, invalid date, bad menu choice, it just asks again instead of breaking.

## How to run it

### What you need

You need **Python 3** installed on your computer. Python is the programming language this program is written in, your computer needs it installed to actually run `.py` files, the same way you need a browser installed to open a website. If you don't have it, download it from [python.org](https://www.python.org/downloads/) and install
it first. Also download Gitbash. You can check if you already have it by running:

```bash
python3 --version
```

### 1. Clone the repository

This downloads a copy of my project onto your own computer.

```bash
git clone https://github.com/Inyange-P/Inyange_Formative1.git
```

### 2. Navigate into the project folder

`cd` means "change directory", it moves your terminal into a specific folder so any command you run after that happens inside it.

```bash
cd Inyange_Formative1
```

### 3. Run the program

```bash
python3 Formative_1.py
```

Follow the menu after that.

## Menu

```
1 to  Add homework
2 to  Add exam
3 to  List assignments
4 to  Filter assignments
5 to  Show summary
0 to  Exit
```

## Example

Adding a homework then checking summary:

```
Enter your choice: 1
You picked Add Homework
Enter subject: math
Enter the assignment title: Algebra HW
Enter the max score: 20
Enter the score you got: 18
Can you Please Enter The Due Date of This Assigment in the format yyyy-mm-dd : 2025-10-05
Homework added!

Enter your choice: 5
You picked Summary
Overall average: 90.0
  math : 90.0
Highest: math Algebra HW 18 / 20
Lowest: math Algebra HW 18 / 20
```

Filtering by subject:

```
Enter your choice: 4
You picked Filter
Filter by subject, type, or month? subject
Enter the value to filter by: math
In math Of Algebra HW You scored 18 / 20 2025-10-05 homework
```

## How I built it

I built the input functions first (asking for score, date, title etc) before anything else, because I wanted to get bad input under control early. After that I made the Assignment class, then Homework and Exam as subclasses of it so I don't repeat the same code twice. GradeTracker came after that to manage the whole list. The menu was
the last thing I connected, once everything else already worked on its own.

## Struggles I had

### Challenges I Faced

* I struggled with wanting to start building before I had fully understood all the concepts I needed, which often meant stopping and going back to learn something first.
* I found it difficult to learn from multiple resources at the same time, especially when switching between YouTube videos, Coursera courses, documentation, and tutorials.
* I often had many ideas and functions in my mind at once, but turning those ideas into a clear and logical order was challenging.
* Sometimes I knew what I wanted the program to do, but I struggled to figure out the best way to structure the code to achieve it.
* Debugging was one of the most challenging parts because finding the exact line or function where a mistake was happening could take a lot of time.
* I sometimes fixed one problem only to discover that the change had affected another part of the project.
* Understanding error messages was difficult at first, especially when I did not immediately understand what was causing the problem.
* I struggled with perfectionism because I wanted every part of the project to be as good as possible, which sometimes made me spend too much time on small details.
* There were moments when trying to make everything perfect actually left me stuck and prevented me from moving forward.
* I sometimes had to change my approach after realizing that the way I had started was not the best way to continue.
* Managing the difference between what I wanted to build and what I realistically had time to build was also challenging.
* I had to learn how to decide which features were important and which ideas could be left for later instead of trying to build everything at once.
* One of the biggest challenges was knowing when to stop improving something and accept that it was good enough to move forward.
* Most importantly, I had to learn that getting stuck, making mistakes, rewriting code, and starting again are all normal parts of programming and not signs that I am failing.


## What I'd improve if I had more time

- Save assignments to a file so they don't disappear when I close it.
- Warn me if a score is really low.
- Let me undo the last thing I added.
- Write actual tests instead of testing everything manually.
