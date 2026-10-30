
# Railway Fare and Reservation Calculator

print("========================================")
print("   RAILWAY FARE AND RESERVATION SYSTEM")
print("========================================")

# Travel class fare rates
print("\nAvailable Travel Classes:")
print("1. Sleeper     - Rs. 1.50 per km")
print("2. AC 3 Tier   - Rs. 2.50 per km")
print("3. AC 2 Tier   - Rs. 3.50 per km")
print("4. AC 1 Tier   - Rs. 5.00 per km")

# Input details
n = int(input("\nEnter number of passengers: "))
distance = float(input("Enter journey distance (km): "))

if n <= 0 or distance <= 0:
    print("Invalid passenger count or distance.")

else:
    choice = int(input("Select travel class (1-4): "))

    rates = {
        1: 1.50,
        2: 2.50,
        3: 3.50,
        4: 5.00
    }

    if choice not in rates:
        print("Invalid travel class.")

    else:
        class_names = {
            1: "Sleeper",
            2: "AC 3 Tier",
            3: "AC 2 Tier",
            4: "AC 1 Tier"
        }

        rate = rates[choice]
        reservation_fee = 40
        cancellation_rate = 0.25

        total_fare = 0
        total_refund = 0
        total_penalty = 0
        total_reservation = 0

        for i in range(1, n + 1):

            print("\nPassenger", i)

            age = int(input("Enter passenger age: "))

            if age < 0:
                print("Invalid age. Enter age again.")
                age = int(input("Enter valid age: "))

            # Calculate basic fare
            basic_fare = distance * rate

            # Age-based concession
            if age < 5:
                concession_rate = 1.0
                category = "Child (Free)"

            elif age <= 11:
                concession_rate = 0.50
                category = "Child"

            elif age >= 60:
                concession_rate = 0.40
                category = "Senior Citizen"

            else:
                concession_rate = 0
                category = "Adult"

            concession = basic_fare * concession_rate
            fare = basic_fare - concession

            # Add reservation fee
            ticket_fare = fare + reservation_fee

            print("\nBasic Fare: Rs.", round(basic_fare, 2))
            print("Concession: Rs.", round(concession, 2))
            print("Reservation Fee: Rs.", reservation_fee)

            cancel = input(
                "Do you want to cancel ticket? (yes/no): "
            ).lower()

            if cancel == "yes":

                penalty = fare * cancellation_rate
                refund = ticket_fare - penalty

                print("Cancellation Penalty: Rs.",
                      round(penalty, 2))
                print("Refund Amount: Rs.",
                      round(refund, 2))

                total_penalty += penalty
                total_refund += refund

            else:
                print("Ticket Confirmed!")
                print("Amount Payable: Rs.",
                      round(ticket_fare, 2))

                total_fare += ticket_fare

            total_reservation += reservation_fee

        # Final summary
        print("\n========================================")
        print("          FINAL RAILWAY SUMMARY")
        print("========================================")

        print("Number of Passengers:", n)
        print("Travel Class:", class_names[choice])
        print("Distance:", distance, "km")
        print("Reservation Fees: Rs.",
              round(total_reservation, 2))
        print("Total Cancellation Penalty: Rs.",
              round(total_penalty, 2))
        print("Total Amount Payable: Rs.",
              round(total_fare, 2))
        print("Total Refund Amount: Rs.",
              round(total_refund, 2))

        print("========================================")
        print("       THANK YOU! HAPPY JOURNEY!")
        print("========================================")

