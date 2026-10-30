
# Attendance Recovery Computation System

import math

print("==============================================")
print("       ATTENDANCE RECOVERY SYSTEM")
print("==============================================")

# Student details
name = input("Enter student name: ")
roll_no = input("Enter roll number: ")

# Attendance details
total_classes = int(input("Enter total classes conducted: "))
attended_classes = int(input("Enter classes attended: "))

required_percentage = float(
    input("Enter required attendance percentage: ")
)

# Validate inputs
if (total_classes <= 0 or attended_classes < 0 or
    attended_classes > total_classes or
    required_percentage <= 0 or
    required_percentage > 100):

    print("\nInvalid Attendance Details!")

else:

    # Calculate current attendance
    current_percentage = (
        attended_classes / total_classes
    ) * 100

    print("\n==============================================")
    print("          ATTENDANCE REPORT")
    print("==============================================")

    print("Student Name :", name)
    print("Roll Number  :", roll_no)
    print("Total Classes:", total_classes)
    print("Attended     :", attended_classes)

    print("Current Attendance:",
          round(current_percentage, 2), "%")

    print("Required Attendance:",
          required_percentage, "%")

    # Check eligibility
    if current_percentage >= required_percentage:

        print("\nEligibility Status: ELIGIBLE")
        print("No recovery classes required.")

    else:

        print("\nEligibility Status: NOT ELIGIBLE")

        # Calculate minimum consecutive classes
        # required when attending every future class
        required_classes = math.ceil(
            (required_percentage * total_classes -
             100 * attended_classes) /
            (100 - required_percentage)
        )

        print("Minimum Consecutive Classes Required:",
              required_classes)

        # Future attendance scenarios
        scenarios = [100, 80, 50]

        print("\n----------------------------------------------")
        print("       FUTURE ATTENDANCE SCENARIOS")
        print("----------------------------------------------")

        for rate in scenarios:

            future_attendance = math.floor(
                required_classes * rate / 100
            )

            future_total = (
                total_classes + required_classes
            )

            future_attended = (
                attended_classes + future_attendance
            )

            future_percentage = (
                future_attended / future_total
            ) * 100

            print("\nFuture Attendance Rate:", rate, "%")

            print("Classes Attended in Future:",
                  future_attendance)

            print("Future Attendance Percentage:",
                  round(future_percentage, 2), "%")

    print("\n==============================================")
    print("       ATTENDANCE ANALYSIS COMPLETED")
    print("==============================================")

