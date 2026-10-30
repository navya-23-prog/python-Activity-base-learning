
# Multi-Currency Travel Budget Analysis System

print("==============================================")
print("      MULTI-CURRENCY TRAVEL BUDGET SYSTEM")
print("==============================================")

# Input traveler details
name = input("Enter traveler name: ")

budget = float(input("Enter planned budget in INR: Rs. "))

n = int(input("Enter number of expense categories: "))

# Validate basic inputs
if budget <= 0 or n <= 0:
    print("Invalid budget or number of categories.")

else:
    total_expense = 0
    total_fee = 0

    largest_expense = 0
    largest_category = ""

    # Process multiple expense categories
    for i in range(1, n + 1):

        print("\nExpense Category", i)

        category = input("Enter category name: ")

        amount = float(
            input("Enter expense amount in foreign currency: ")
        )

        rate = float(
            input("Enter exchange rate (INR per unit): ")
        )

        fee_percentage = float(
            input("Enter conversion fee percentage: ")
        )

        # Validate expense details
        if (amount < 0 or rate <= 0 or
            fee_percentage < 0):

            print("Invalid expense details!")
            break

        # Convert currency into INR
        converted_amount = amount * rate

        # Calculate conversion fee
        conversion_fee = (
            converted_amount * fee_percentage / 100
        )

        # Calculate final category expense
        category_expense = converted_amount + conversion_fee

        # Add to total expenditure
        total_expense += category_expense
        total_fee += conversion_fee

        # Find largest expense category
        if category_expense > largest_expense:
            largest_expense = category_expense
            largest_category = category

        # Display category details
        print("\nConverted Amount: Rs.",
              round(converted_amount, 2))

        print("Conversion Fee: Rs.",
              round(conversion_fee, 2))

        print("Total Category Expense: Rs.",
              round(category_expense, 2))

    else:
        # Compare expenditure with budget
        difference = budget - total_expense

        if total_expense <= budget:
            status = "WITHIN BUDGET"
        else:
            status = "BUDGET EXCEEDED"

        # Display final report
        print("\n==============================================")
        print("          TRAVEL BUDGET REPORT")
        print("==============================================")

        print("Traveler Name       :", name)
        print("Planned Budget      : Rs.", round(budget, 2))

        print("----------------------------------------------")
        print("Total Conversion Fees: Rs.",
              round(total_fee, 2))

        print("Total Travel Expense: Rs.",
              round(total_expense, 2))

        print("Largest Expense Category:", largest_category)

        print("Largest Category Amount: Rs.",
              round(largest_expense, 2))

        print("----------------------------------------------")

        if difference >= 0:
            print("Remaining Budget   : Rs.",
                  round(difference, 2))
        else:
            print("Budget Exceeded By : Rs.",
                  round(abs(difference), 2))

        print("Budget Status      :", status)

        print("==============================================")
        print("      TRAVEL ANALYSIS COMPLETED")
        print("==============================================")

