
# ATM Transaction Sequence Simulation

# Read initial account details
balance = float(input("Enter initial account balance: "))
daily_limit = float(input("Enter daily withdrawal limit: "))

# Read number of transactions
n = int(input("Enter number of transactions: "))

# Initialize variables
total_deposits = 0
total_withdrawals = 0

successful_transactions = 0
rejected_transactions = 0

print("\n========== ATM TRANSACTION DETAILS ==========")

for i in range(1, n + 1):

    print("\nTransaction", i)

    transaction_type = input(
        "Enter transaction type (Deposit/Withdrawal): "
    ).lower()

    amount = float(input("Enter transaction amount: "))

    # Check invalid amount
    if amount <= 0:
        print("Transaction Rejected: Invalid amount.")
        rejected_transactions += 1

    # Deposit operation
    elif transaction_type == "deposit":

        balance = balance + amount
        total_deposits += amount

        successful_transactions += 1

        print("Deposit Successful.")
        print("Updated Balance:", balance)

    # Withdrawal operation
    elif transaction_type == "withdrawal":

        if amount > balance:
            print("Transaction Rejected: Insufficient balance.")
            rejected_transactions += 1

        elif total_withdrawals + amount > daily_limit:
            print("Transaction Rejected: Daily withdrawal limit exceeded.")
            rejected_transactions += 1

        else:
            balance = balance - amount
            total_withdrawals += amount

            successful_transactions += 1

            print("Withdrawal Successful.")
            print("Updated Balance:", balance)

    # Invalid transaction type
    else:
        print("Transaction Rejected: Invalid transaction type.")
        rejected_transactions += 1

# Display transaction summary
print("\n========== ATM TRANSACTION SUMMARY ==========")

print("Total Deposits:", total_deposits)
print("Total Withdrawals:", total_withdrawals)

print("Successful Transactions:", successful_transactions)
print("Rejected Transactions:", rejected_transactions)

print("Final Account Balance:", balance)

print("Remaining Daily Withdrawal Limit:",
      daily_limit - total_withdrawals)

print("\n========== THANK YOU ==========")

