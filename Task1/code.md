# 3. Hospital Billing and Patient Classification System Using Python

## 1. Problem Statement

Develop a Python program for a Hospital Billing and Patient Classification System. The system calculates the total hospital bill based on consultation charges, diagnostic charges, and treatment charges.

The program applies conditional concessions depending on the patient's category. It validates billing constraints to ensure that charges are not negative and that the entered values are valid.

Finally, patients are classified according to their payment policy, such as:

- Fully Paid: Patient has paid the complete bill.
- Partially Paid: Patient has paid some amount but still has a balance.
- Unpaid: Patient has not paid any amount.

The system displays the total bill, concession amount, final payable amount, payment details, and patient classification.

## 2. Algorithm

1. Start the program.
2. Enter the patient's name and age.
3. Enter consultation charges.
4. Enter diagnostic charges.
5. Enter treatment charges.
6. Validate all charges. If any charge is negative, display an error.
7. Calculate the total bill by adding all three charges.
8. Check the patient's category.
   - If the patient is a senior citizen (age 60 or above), apply a 10% concession.
   - Otherwise, if the total bill is above ₹10,000, apply a 5% concession.
   - Otherwise, no concession is applied.
9. Calculate the final payable amount.
10. Enter the amount paid by the patient.
11. Validate the payment amount.
12. Classify the patient:
    - If payment equals the final bill, classify as Fully Paid.
    - If payment is greater than zero but less than the final bill, classify as Partially Paid.
    - If payment is zero, classify as Unpaid.
13. Calculate the remaining balance.
14. Display the complete billing details.
15. Stop the program.
```mermaid
## 3. Flowchart 

flowchart TD
    A([Start]) --> B[/Enter patient name and age/]
    B --> C[/Enter consultation charges/]
    C --> D[/Enter diagnostic charges/]
    D --> E[/Enter treatment charges/]
    E --> F{Are all charges non-negative?}
    F -- No --> G[/Display Invalid Charges/]
    G --> Z([Stop])
    F -- Yes --> H[Calculate Total Bill]
    H --> I{Age >= 60?}
    I -- Yes --> J[Apply 10% Concession]
    I -- No --> K{Total Bill > 10000?}
    K -- Yes --> L[Apply 5% Concession]
    K -- No --> M[No Concession]
    J --> N[Calculate Final Payable Amount]
    L --> N
    M --> N
    N --> O[/Enter Amount Paid/]
    O --> P{Is Payment Valid?}
    P -- No --> Q[/Display Invalid Payment/]
    Q --> Z
    P -- Yes --> R{Amount Paid = Final Bill?}
    R -- Yes --> S[Fully Paid]
    R -- No --> T{Amount Paid > 0?}
    T -- Yes --> U[Partially Paid]
    T -- No --> V[Unpaid]
    S --> W[Calculate Balance]
    U --> W
    V --> W
    W --> X[/Display Billing Details/]
    X --> Z([Stop])
```

## 5. Sample Input

Patient Details

```
Enter patient name: Rahul
Enter patient age: 65
Enter consultation charges: Rs. 500
Enter diagnostic charges: Rs. 2500
Enter treatment charges: Rs. 7000
Enter amount paid: Rs. 7000
```

## 6. Sample Output

Hospital Billing System

Partially Paid

```
----------- BILL DETAILS -----------

Patient Name: Rahul
Patient Age: 65
Patient Category: Senior Citizen

Consultation Charges: Rs. 500
Diagnostic Charges: Rs. 2500
Treatment Charges: Rs. 7000

Total Bill: Rs. 10000
Concession: Rs. 1000
Final Payable Amount: Rs. 9000

========== PAYMENT SUMMARY ==========

Total Bill: Rs. 10000
Concession: Rs. 1000
Final Amount: Rs. 9000
Amount Paid: Rs. 7000
Remaining Balance: Rs. 2000

Payment Status: Partially Paid

=====================================
           THANK YOU!
=====================================
```

## 7. Explanation of Concepts Used

| Python concept         | Application                           |
| ---------------------- | ------------------------------------- |
| Variables              | Store patient details and charges     |
| Input statements       | Accept patient information            |
| Data types             | Integer, float and string             |
| Arithmetic operators   | Calculate bill and concession         |
| Conditional statements | Apply discounts and classify patients |
| Comparison operators   | Validate age, charges and payment     |
| Type conversion        | Convert input into integer and float  |
| Print statements       | Display billing details               |

