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


