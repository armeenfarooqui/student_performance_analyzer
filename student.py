# Name: Armeen Farooqui
# Period: AM
# Student Performance Analyzer


print("========================================")
print("       STUDENT PERFORMANCE ANALYZER")
print("========================================")
print()
print("Enter the student's information below.")

# Student Information
student_name = input("What is the student's name? ")
grade_level = int(input("What grade level is the student in? "))
assignment_average = float(input("What is the student's assignment average? "))
quiz_average = float(input("What is the student's quiz average? "))
test_average = float(input("What is the student's test average? "))
attendance_percentage = float(input("What is the student's attendance percentage? "))
missing_assignments = int(input("How many missing assignments does the student have? "))


# Calculate the Overall Grade
def calculate_grade(assignment_average, quiz_average, test_average):
    assignment_portion = assignment_average * 0.30
    quiz_portion = quiz_average * 0.30
    test_portion = test_average * 0.40

    overall_grade = assignment_portion + quiz_portion + test_portion

    print("Overall Grade:", overall_grade)
    return overall_grade


overall_grade = calculate_grade(assignment_average,quiz_average,test_average)


# Determine Letter Grade
def letter_grade(overall_grade):
    if overall_grade >= 90:
        letter = "A"
    elif overall_grade >= 80:
        letter = "B"
    elif overall_grade >= 70:
        letter = "C"
    elif overall_grade >= 60:
        letter = "D"
    else:
        letter = "F"

    print("Letter Grade:", letter)


letter_grade(overall_grade)


# Determine Attendance Status
def attendance_status(attendance):
    if attendance >= 95:
        status = "Excellent Attendance"
    elif attendance >= 90:
        status = "Good Attendance"
    elif attendance >= 80:
        status = "Attendance Warning"
    else:
        status = "Poor Attendance"

    print("Attendance Status:", status)
attendance_status(attendance_percentage)

def assignment_status(missing_assignments):
    if missing_assignments == 0:
        print("Missing Assignment Status: Excellent")
    elif missing_assignments <= 2:
        print("Missing Assignment Status: Good")
    elif missing_assignments <= 4:
        print("Missing Assignment Status: Warning")
    else:
        print("Missing Assignment Status: Critical")


# Part 7 — Academic Eligibility

def check_eligibility(overall_grade, attendance, missing_assignments):
    if overall_grade >= 70:
        if attendance >= 90:
            if missing_assignments <= 2:
                print("Academic Eligibility: ELIGIBLE")
                print("Student passed all three requirements.")
            else:
                print("Academic Eligibility: NOT ELIGIBLE")
                print("Reason: Too many missing assignments.")
        else:
            print("Academic Eligibility: NOT ELIGIBLE")
            print("Reason: Attendance is too low.")
    else:
        print("Academic Eligibility: NOT ELIGIBLE")
        print("Reason: Overall grade is too low.")


# Part 8 — High Honors

def check_high_honors(overall_grade, attendance, missing_assignments):
    if overall_grade >= 90:
        if attendance >= 95:
            if missing_assignments == 0:
                print("High Honors: YES")
            else:
                print("High Honors: NO")
                print("Reason: Student has missing assignments.")
        else:
            print("High Honors: NO")
            print("Reason: Attendance requirement not met.")
    else:
        print("High Honors: NO")
        print("Reason: Grade requirement not met.")


# Part 9 — Using and

def check_good_standing(overall_grade, attendance):
    if overall_grade >= 70 and attendance >= 90:
        print("Good Standing: YES")
    else:
        print("Good Standing: NO") 

# Part 10 — Using or 

def check_support(overall_grade, attendance):
    if overall_grade < 70 or attendance < 80:
        print("Additional Support: RECOMMENDED")
    else:
        print("Additional Support: NOT NEEDED")

# Part 11 — Student Login

# Ask the user for their username
username = input("Enter username: ")

# Ask the user for their PIN
pin = input("Enter PIN: ")

# Check the username first
if username == "student":
    # Check the PIN if the username is correct
    if pin == "1234":
        print("Login Successful!")
    else:
        print("Login Failed: Incorrect PIN.")
else:
    print("Login Failed: Incorrect username.")


# Part 12 — Grade-Level Message

def grade_level_message(grade_level):
    # Check which grade level the student entered
    if grade_level == 9:
        print("Welcome to your freshman year!")
    elif grade_level == 10:
        print("Keep building your skills!")
    elif grade_level == 11:
        print("Junior year — keep pushing!")
    elif grade_level == 12:
        print("Senior year — finish strong!")
    else:
        print("Invalid grade level.")


# Part 13 — Strongest Academic Category

def strongest_category(assignment_average, quiz_average, test_average):
    # Check if assignments are the highest
    if assignment_average >= quiz_average:
        if assignment_average >= test_average:
            print("Strongest Category: Assignments")
        else:
            print("Strongest Category: Tests")
    else:
        # Check if quizzes are higher than tests
        if quiz_average >= test_average:
            print("Strongest Category: Quizzes")
        else:
            print("Strongest Category: Tests")


# Part 14 — Student Summary

# Print the student's information
print()
print("========================================")
print("          STUDENT SUMMARY")
print("========================================")

print("Student:", username)
print("Grade Level:", grade_level)

print()
print("Assignment Average:", assignment_average)
print("Quiz Average:", quiz_average)
print("Test Average:", test_average)

print()
print("Overall Grade:", overall_grade)
print("Attendance:", attendance)
print("Missing Assignments:", missing_assignments)

print("========================================")