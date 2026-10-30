# Railway Fare and Reservation Calculator Using Python.

## 1. Problem Statement

Develop a Python program for a Railway Fare and Reservation Calculator that calculates ticket fares for multiple passengers based on distance, travel class, age-based concessions, reservation fees, and cancellation penalties.

The system accepts the number of passengers, journey distance, travel class, and passenger age. It calculates the basic fare using predefined distance slabs and applies different fare rates according to the selected travel class.

Age-based concessions are provided for eligible passengers:

- Children below 5 years: Free travel.
- Children aged 5 to 11 years: 50% concession.
- Senior citizens aged 60 and above: 40% concession.
- Other passengers: No concession.

A reservation fee is added to each passenger's ticket. If a passenger cancels the ticket, the system calculates the cancellation penalty and displays the refund amount.

Finally, the program displays the total fare, concession, reservation fee, cancellation penalty, and final payable or refundable amount.

## 2. Algorithm

1. Start the program.
2. Enter the number of passengers.
3. Enter the journey distance in kilometres.
4. Validate the distance and passenger count.
5. Select the travel class:
   - Sleeper – ₹1.50 per km
   - AC 3 Tier – ₹2.50 per km
   - AC 2 Tier – ₹3.50 per km
   - AC 1 Tier – ₹5.00 per km
6. Calculate the basic fare based on distance and class.
7. Enter the age of each passenger.
8. Apply age-based concessions:
   - Below 5 years: 100% concession.
   - 5–11 years: 50% concession.
   - 60 years and above: 40% concession.
   - Others: No concession.
9. Add a reservation fee of ₹40 per passenger.
10. Calculate the total ticket amount.
11. Ask whether the passenger wants to cancel the ticket.
12. If cancellation is selected, apply a 25% cancellation penalty on the fare after concession (excluding reservation fee).
13. Calculate the refund amount after deducting the penalty and reservation fee.
14. Display the passenger-wise and total billing details.
15. Stop the program.

## 3. Flowchart 
```Mermaid

flowchart TD
    A([Start]) --> B[/Enter number of passengers/]
    B --> C[/Enter journey distance/]
    C --> D{Valid inputs?}
    D -- No --> E[/Display error message/]
    E --> Z([Stop])
    D -- Yes --> F[/Select travel class/]
    F --> G[Calculate basic fare]
    G --> H[/Enter passenger age/]
    H --> I{Age below 5?}
    I -- Yes --> J[Apply 100% concession]
    I -- No --> K{Age between 5 and 11?}
    K -- Yes --> L[Apply 50% concession]
    K -- No --> M{Age 60 or above?}
    M -- Yes --> N[Apply 40% concession]
    M -- No --> O[No concession]
    J --> P[Calculate fare after concession]
    L --> P
    N --> P
    O --> P
    P --> Q[Add reservation fee]
    Q --> R{Cancel ticket?}
    R -- Yes --> S[Calculate 25% penalty]
    S --> T[Calculate refund amount]
    R -- No --> U[Calculate payable amount]
    T --> V[/Display ticket details/]
    U --> V
    V --> W{More passengers?}
    W -- Yes --> H
    W -- No --> X[/Display total bill and refund/]
    X --> Z([Stop])
```
## 4. Sample Input

Railway Reservation Details

```
Enter number of passengers: 3
Enter journey distance (km): 500
Select travel class (1-4): 1

Passenger 1
Enter passenger age: 30
Do you want to cancel ticket? (yes/no): no

Passenger 2
Enter passenger age: 65
Do you want to cancel ticket? (yes/no): no

Passenger 3
Enter passenger age: 10
Do you want to cancel ticket? (yes/no): yes
```

## 5. Sample Output

Railway Reservation Summary

Calculated

```
========================================
Passenger 1

Basic Fare: Rs. 750.0
Concession: Rs. 0.0
Reservation Fee: Rs. 40
Ticket Confirmed!
Amount Payable: Rs. 790.0

Passenger 2

Basic Fare: Rs. 750.0
Concession: Rs. 300.0
Reservation Fee: Rs. 40
Ticket Confirmed!
Amount Payable: Rs. 490.0

Passenger 3

Basic Fare: Rs. 750.0
Concession: Rs. 375.0
Reservation Fee: Rs. 40
Cancellation Penalty: Rs. 93.75
Refund Amount: Rs. 321.25

========================================
        FINAL RAILWAY SUMMARY
========================================

Number of Passengers: 3
Travel Class: Sleeper
Distance: 500 km

Reservation Fees: Rs. 120.0
Total Cancellation Penalty: Rs. 93.75
Total Amount Payable: Rs. 1280.0
Total Refund Amount: Rs. 321.25

========================================
     THANK YOU! HAPPY JOURNEY!
========================================
```

## 6. Explanation of Python Concepts Used

| Concept                | Application                                |
| ---------------------- | ------------------------------------------ |
| Variables              | Store passenger details and fares          |
| Input statements       | Accept passenger information               |
| Data types             | Integer, float and string                  |
| Dictionary             | Store travel class fare rates              |
| Arithmetic operators   | Calculate fares, concessions and penalties |
| Conditional statements | Apply age concessions                      |
| For loop               | Process multiple passengers                |
| Comparison operators   | Check passenger age and travel class       |
| Type conversion        | Convert input into numeric values          |
| Print statements       | Display ticket and refund details          |

