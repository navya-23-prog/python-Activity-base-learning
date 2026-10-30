
# Examination Result and Grace-Mark Validation System

print("==============================================")
print("    EXAMINATION RESULT MANAGEMENT SYSTEM")
print("==============================================")

# Student details
name = input("Enter student name: ")
roll_no = input("Enter roll number: ")

# Examination details
n = int(input("Enter number of subjects: "))
max_marks = int(input("Enter maximum marks per subject: "))
pass_marks = int(input("Enter minimum passing marks: "))
grace_limit = int(input("Enter grace mark limit: "))

# Validate examination rules
if (n <= 0 or max_marks <= 0 or
    pass_marks <= 0 or pass_marks > max_marks or
    grace_limit < 0 or grace_limit > max_marks):

    print("\nInvalid examination details!")

else:

    subjects = []
    marks = []
    failed_subjects = []

    valid = True

    # Enter subject details
    for i in range(n):

        print("\nSubject", i + 1)

        subject = input("Enter subject name: ")
        mark = int(input("Enter marks obtained: "))

        if mark < 0 or mark > max_marks:
            print("Invalid marks entered!")
            valid = False
            break

        subjects.append(subject)
        marks.append(mark)

    if valid:

        # Identify failed subjects
        for i in range(n):

            if marks[i] < pass_marks:
                failed_subjects.append(i)

        grace_awarded = 0

        # Apply grace-mark policy
        if len(failed_subjects) == 1:

            index = failed_subjects[0]

            shortage = pass_marks - marks[index]

            if shortage <= grace_limit:

                required_grace = shortage

                # Ensure marks do not exceed maximum
                if marks[index] + required_grace <= max_marks:

                    marks[index] += required_grace
                    grace_awarded = required_grace

        # Check final result
        all_passed = True

        for mark in marks:

            if mark < pass_marks:
                all_passed = False

        # Classify student
        if all_passed and grace_awarded > 0:
            result = "PASS WITH GRACE"

        elif all_passed:
            result = "PASS"

        else:
            result = "FAIL"

        # Calculate total and percentage
        total_marks = sum(marks)
        total_maximum = n * max_marks

        percentage = (total_marks / total_maximum) * 100

        # Display result
        print("\n==============================================")
        print("          EXAMINATION RESULT")
        print("==============================================")

        print("Student Name :", name)
        print("Roll Number  :", roll_no)

        print("----------------------------------------------")
        print("             SUBJECT DETAILS")
        print("----------------------------------------------")

        for i in range(n):

            print(subjects[i], ":", marks[i],
                  "/", max_marks)

        print("----------------------------------------------")

        print("Grace Marks Awarded :", grace_awarded)

        print("Total Marks Obtained:", total_marks)

        print("Maximum Total Marks :", total_maximum)

        print("Percentage          :", round(percentage, 2), "%")

        print("----------------------------------------------")

        print("Final Result        :", result)

        print("==============================================")
        print("       RESULT GENERATED SUCCESSFULLY")
        print("==============================================")

