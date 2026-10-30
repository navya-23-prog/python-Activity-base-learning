
# Hospital Billing and Patient Classification System

print("======================================")
print("     HOSPITAL BILLING SYSTEM")
print("======================================")

# Patient details
name = input("Enter patient name: ")
age = int(input("Enter patient age: "))

# Input hospital charges
consultation = float(input("Enter consultation charges: Rs. "))
diagnostic = float(input("Enter diagnostic charges: Rs. "))
treatment = float(input("Enter treatment charges: Rs. "))

# Validate charges
if age < 0 or consultation < 0 or diagnostic < 0 or treatment < 0:
    print("\nInvalid Input! Age and charges cannot be negative.")

else:
    # Calculate total bill
    total_bill = consultation + diagnostic + treatment

    # Apply conditional concessions
    if age >= 60:
        concession = total_bill * 0.10
        category = "Senior Citizen"

    elif total_bill > 10000:
        concession = total_bill * 0.05
        category = "Regular Patient"

    else:
        concession = 0
        category = "Regular Patient"

    # Calculate final payable amount
    final_bill = total_bill - concession

    print("\n----------- BILL DETAILS -----------")
    print("Patient Name:", name)
    print("Patient Age:", age)
    print("Patient Category:", category)
    print("Consultation Charges: Rs.", consultation)
    print("Diagnostic Charges: Rs.", diagnostic)
    print("Treatment Charges: Rs.", treatment)
    print("Total Bill: Rs.", total_bill)
    print("Concession: Rs.", concession)
    print("Final Payable Amount: Rs.", final_bill)

    # Enter payment
    paid = float(input("\nEnter amount paid: Rs. "))

    # Validate payment
    if paid < 0 or paid > final_bill:
        print("Invalid Payment! Enter an amount between 0 and the final bill.")

    else:
        balance = final_bill - paid

        # Patient classification
        if paid == final_bill:
            status = "Fully Paid"

        elif paid > 0:
            status = "Partially Paid"

        else:
            status = "Unpaid"

        # Display final details
        print("\n========== PAYMENT SUMMARY ==========")
        print("Total Bill: Rs.", round(total_bill, 2))
        print("Concession: Rs.", round(concession, 2))
        print("Final Amount: Rs.", round(final_bill, 2))
        print("Amount Paid: Rs.", round(paid, 2))
        print("Remaining Balance: Rs.", round(balance, 2))
        print("Payment Status:", status)

        print("=====================================")
        print("       THANK YOU!")
        print("=====================================")

