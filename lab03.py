########################################################################
##
## CS 101 Lab
## Program #1
## Daylan Quinn
## drq9q7@mail.umkc.edu
##
## PROBLEM : Adjust the inputed results for weighted grades to give a final grade
##
## ALGORITHM :
##      1. Get input for indivdual grades in labs, exams, and attendance
##      2. Calculte weighted totals and add together
##      3. Output the weighted grade with a corresponding letter grade
##
## ERROR HANDLING:
##      Got a little caught up in the assignment and think i handled errors well
##
## OTHER COMMENTS:
##      Made it round up an extra .1 because im a generous instructor
##      
##
########################################################################

def check_val(grade):
    """Changes the value if it is above 100 or below 0"""
    while (grade < 0) or (grade > 100):
        if grade < 0:
            print("Value changed to 0")
            grade = 0
        if grade > 100:
            print("Value changed to 100")
            grade = 100
    return grade


def check_type(grade):
    """Makes sure the value is number and makes it a float"""
    while True:  
        try:
            grade = float(grade)
            return grade
        except:
            grade = input("input must be a number (ex. 95, 86.4) -> ")


#MAIN

#GATHER APPROPRIATE DATA TO BE ADDED TO TOTAL WEIGHTED GRADE
labs = input("Enter your grade from 0-100 for the weighted cagegory of Labs (70%) -> ")
labs = check_val(check_type(labs))

exams = input("Enter your grade from 0-100 for the weighted cagegory of Lab Exams (20%) -> ")
exams = check_val(check_type(exams))

attend = input("Enter your grade from 0-100 for the weighted cagegory of Attendance (10%) -> ")
attend = check_val(check_type(attend))

#WEIGHTS THE GRADES
labs = labs * 0.7
exams = exams * 0.2
attend = attend * 0.1

#ADDS TO CREATE TOTAL
total = round(labs + exams + attend, 1)

#GIVES APPROPRIATE GRADE BASED ON TOTAL GRADE
if total >= 90:
    print("Your overall grade is an A with", total, "%")
elif (total >= 80) & (total < 90):
    print("Your overall grade is a B with", total, "%")
elif (total >= 70) & (total < 80):
    print("Your overall grade is a C with", total, "%")
elif (total >= 60) & (total < 70):
    print("Your overall grade is a D with", total, "%")
else:
    print("Your overall grade is a F with", total, "%")

