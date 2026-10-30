
# Employee Payroll and Deduction Analysis System

print("==========================================")
print("       EMPLOYEE PAYROLL SYSTEM")
print("==========================================")

# Employee details
name = input("Enter employee name: ")
emp_id = input("Enter employee ID: ")

# Salary details
basic = float(input("Enter basic salary: Rs. "))
allowances = float(input("Enter allowances: Rs. "))
overtime_hours = float(input("Enter overtime hours: "))
overtime_rate = float(input("Enter overtime rate per hour: Rs. "))
incentives = float(input("Enter incentives: Rs. "))

# Validate inputs
if (basic < 0 or allowances < 0 or
    overtime_hours < 0 or overtime_rate < 0 or
    incentives < 0):

    print("\nInvalid Input! Values cannot be negative.")

else:
    # Calculate overtime pay
    overtime_pay = overtime_hours * overtime_rate

    # Calculate gross salary
    gross_salary = (basic + allowances +
                    overtime_pay + incentives)

    # Apply progressive deduction rate
    if gross_salary <= 20000:
        deduction_rate = 0

    elif gross_salary <= 40000:
        deduction_rate = 0.05

    elif gross_salary <= 60000:
        deduction_rate = 0.10

    else:
        deduction_rate = 0.15

    # Calculate deductions
    deduction = gross_salary * deduction_rate

    # Calculate net salary
    net_salary = gross_salary - deduction

    # Display salary statement
    print("\n==========================================")
    print("          SALARY STATEMENT")
    print("==========================================")

    print("Employee Name       :", name)
    print("Employee ID         :", emp_id)

    print("------------------------------------------")
    print("             EARNINGS")
    print("------------------------------------------")

    print("Basic Salary        : Rs.", round(basic, 2))
    print("Allowances          : Rs.", round(allowances, 2))
    print("Overtime Pay        : Rs.", round(overtime_pay, 2))
    print("Incentives          : Rs.", round(incentives, 2))

    print("------------------------------------------")
    print("Gross Salary        : Rs.", round(gross_salary, 2))
    print("Deduction Rate      :", deduction_rate * 100, "%")
    print("Total Deduction     : Rs.", round(deduction, 2))

    print("------------------------------------------")
    print("Net Salary          : Rs.", round(net_salary, 2))
    print("==========================================")
    print("       PAYROLL GENERATED SUCCESSFULLY")
    print("==========================================")

