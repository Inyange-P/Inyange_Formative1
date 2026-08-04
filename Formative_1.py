# STEP 1: I need a function that asks the user whether an assignment is Homework or Exam, and keeps asking until they type one of those two
# valid options. I'll use a while loop so it doesn't stop until the input is valid, and .lower() so it doesn't matter if they type  uppercase or lowercase.

def Get_Assignment_Type():
    while True:
        Assignment_Type = str(input("Enter if the assignment is Homework or Exam: "))
        if Assignment_Type.lower() == "homework" or Assignment_Type.lower() == "exam":
            return Assignment_Type
        else:
            print("Invalid input. Please type Homework or Exam.")

# STEP 2: I need a function to collect the assignment's title and its max score. I return both values together so whoever calls this
# function can use them right away.
    
def GetTitle_and_Max_core():
    Title = input("Enter the assignment title: ")
    Max_score = int(input("Enter the max score: "))
    return Title, Max_score

# STEP 3: I need a function that asks for the score the student got,and makes sure it's a valid number: not negative, and not higher than the max score. I take max_score in as a parameter so I can
# check against it. I use a while loop so it keeps asking until the score passes both checks, only returning once it's valid.

def Gotten_Score(Max_score):
    while True:
     GottenScore = int(input("Enter the score you got: "))
     if GottenScore > Max_score:
        print("Error: The score cannot exceed the maximum marks.")
     elif GottenScore < 0:
        print("Error: The score cannot be negative.")
     else:
        return GottenScore


# STEP 4: I need a function to collect the due date and make sure it's a real, valid date in YYYY-MM-DD format. I use try/except with
# datetime.strptime() to check this, since checking a real calendar date by hand (leap years, days per month) would be complicated.
# I loop until a valid date is entered.

def Get_The_Due_Date ():
   while True:
    The_Due_Date = str (input("Can you Please Enter The Due Date of This Assigment in the format yyyy-mm-dd : "))
    from datetime import datetime
    try:
      datetime.strptime(The_Due_Date, "%Y-%m-%d")
      return The_Due_Date
    except ValueError:
      print("That's not a valid date!")


# STEP 5: This is my base class. Every assignment (homework or exam) needs to store the same 6 pieces of information: subject, title,
# score, max_score, due_date, and type. I put all of this in one class so I don't have to track 6 separate lists that could get out
# of sync with each other.

class Assignment:
    def __init__( self, new_subject, new_title, new_score, new_max_score, new_due_date, new_type):
        self.subject = new_subject
        self.title = new_title
        self.score = new_score
        self.max_score = new_max_score
        self.due_date = new_due_date
        self.type = new_type

# STEP 6: Homework is a subclass of Assignment. It inherits everything Assignment already knows how to do, so I don't have to rewrite the
# same __init__ logic again. I only need to ask for 5 things (not type), because I use super() to call Assignment's __init__ and
# hardcode "homework" as the type automatically.


class Homework(Assignment):
    def __init__(self, new_subject, new_title, new_score, new_max_score, new_due_date):
        super().__init__(new_subject, new_title, new_score, new_max_score, new_due_date, "homework")

# Code Check:

# hw1 = Homework("Math", "Chapter 4 HW", 45, 50, "2025-12-10")
# print(hw1.subject, hw1.title, hw1.score, hw1.type)
# STEP 7: Same idea as Homework, but this time the type is automatically set to "exam" instead. This is the second subclass
# required by the assignment, proving Assignment can be reused for more than one kind of assignment.

class Exam(Assignment):
   def __init__(self, new_subject, new_title, new_score, new_max_score, new_due_date):
      super().__init__(new_subject, new_title, new_score, new_max_score, new_due_date, "exam")

# Code check:

# exam1 = Exam("Matehmatics", "Chapter 5", 22, 100, "2026-12-3")
# print (exam1.score)

# STEP 8: This class is the "manager" of my whole program. Instead of using one loose list, I bundle the list of assignments together
# with all the actions I can do on it (add, list, filter, summarize) into one class, so everything related to managing assignments lives
# in one place.

class GradeTracker():
# I start with just one empty list. Nothing is passed in here because a tracker doesn't need any data to exist, it just needs to be ready to store assignments as they're added.  
   def __init__(self):
      self.assignments = []

#Code check:
# my_tracker = GradeTracker()
# print(my_tracker.assignments)
# This method takes one Assignment object (could be Homework or Exam, since both inherit from Assignment) and adds it onto the end of my list, without erasing anything already stored there.

   def add_assignment(self, new_assignment):
       self.assignments.append(new_assignment)

# This method loops through every assignment I've stored so far and prints each one in a readable line. This is what powers
# menu option 3 (List Assignments).

   def list_assignments(self):
     for assignment in self.assignments:
        print("In ",assignment.subject,"Of ", assignment.title, "You scored ", assignment.score, "out of", assignment.max_score, "and the due date was ", assignment.due_date, ".It was ", assignment.type)

#code check:

# my_tracker = GradeTracker()
# print(my_tracker.assignments)

# my_tracker = GradeTracker()
# my_tracker.add_assignment(hw1)
# my_tracker.add_assignment(exam1)
# print(len(my_tracker.assignments))
# print(my_tracker.assignments[0].subject)
# print(my_tracker.assignments[1].subject)
# my_tracker.list_assignments()

   def filter_by_type(self, type_wanted):
     for assignment in self.assignments:
        if assignment.type == type_wanted:
            print("In", assignment.subject, "Of", assignment.title, "You scored", assignment.score, "/", assignment.max_score, assignment.due_date, assignment.type)

# Code check :

# my_tracker = GradeTracker()
# my_tracker.filter_by_type("homework")
# This method lets me filter my assignments by subject, type, or month. filter_by tells the method which field to check, and
# value is what I'm looking for. Month filtering uses.startswith() because due_date is a full date, and I only want to match the year-month part of it. This powers menu option 4.

   def filter_assignments(self, filter_by, value):
    for assignment in self.assignments:
        if filter_by == "subject" and assignment.subject == value:
            print("In", assignment.subject, "Of", assignment.title, "You scored", assignment.score, "/", assignment.max_score, assignment.due_date, assignment.type)
        elif filter_by == "type" and assignment.type == value:
            print("In", assignment.subject, "Of", assignment.title, "You scored", assignment.score, "/", assignment.max_score, assignment.due_date, assignment.type)
        elif filter_by == "month" and assignment.due_date.startswith(value):
            print("In", assignment.subject, "Of", assignment.title, "You scored", assignment.score, "/", assignment.max_score, assignment.due_date, assignment.type)

# Code check:
# my_tracker.filter_assignments("subject", "math")
# my_tracker.filter_assignments("type", "exam")
# my_tracker.filter_assignments("month", "2025-12")

# hw1_percentage = (hw1.score / hw1.max_score) * 100
# print(hw1_percentage)

# exam1_percentage = (exam1.score / exam1.max_score) * 100
# print(exam1_percentage)

# This method calculates and prints everything for menu option 5:
# 1) the overall average across ALL assignments (mixing homework and exams together), by turning each score into a percentage first and then averaging those percentages
# 2) the average per subject, using a dictionary to group percentages by subject before averaging each group
# 3) the single highest and lowest scoring assignment, found by comparing percentages as I loop through the list
# I also have to check for an empty list first, so the program doesn't crash by dividing by zero if no assignments exist yet.
 
   def show_summary(self):
     total_percentage = 0
     for assignment in self.assignments:
        percentage = (assignment.score / assignment.max_score) * 100
        total_percentage = total_percentage + percentage

# Part 1: overall average
     overall_average = total_percentage / len(self.assignments)
     print("Overall average:", overall_average)

# Part 2: per-subject averages, grouped using a dictionary
     subject_scores = {}
     for assignment in self.assignments:
       percentage = (assignment.score / assignment.max_score) * 100 
       if assignment.subject not in subject_scores:
          subject_scores[assignment.subject] = []    
       subject_scores[assignment.subject].append(percentage)
     for subject, scores in subject_scores.items():
      subject_average = sum(scores) / len(scores)
      print(" ", subject, ":", subject_average)

# Find the Highest scoring assignment
     highest = self.assignments[0]
     for assignment in self.assignments:
        if (assignment.score / assignment.max_score) * 100 > (highest.score / highest.max_score) * 100:
            highest = assignment
     print("Highest:", highest.subject, highest.title, highest.score, "/", highest.max_score)

# Find the Lowest scoring assignment
     lowest = self.assignments[0]
     for assignment in self.assignments:
        if (assignment.score / assignment.max_score) * 100 < (lowest.score / lowest.max_score) * 100:
            lowest = assignment
     print("Lowest:", lowest.subject, lowest.title, lowest.score, "/", lowest.max_score)


# I create ONE tracker here, before the menu loop starts, so it persists across every menu choice. If I created it inside the loop,  it would reset to empty every time, and I'd lose all my data.

my_tracker = GradeTracker()

# The my main menu loop. It keeps showing the menu and asking for a choice until the user picks 0 to exit. I use if/elif to route each choice to the right action.

