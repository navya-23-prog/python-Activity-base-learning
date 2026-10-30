
# Warehouse Inventory Reconciliation

products = []

n = int(input("Enter the number of products: "))

for i in range(n):
    print("\nEnter details for Product", i + 1)

    name = input("Product name: ")
    opening = int(input("Opening stock: "))
    incoming = int(input("Incoming quantity: "))
    dispatched = int(input("Dispatched quantity: "))
    actual_closing = int(input("Actual closing stock: "))
    minimum_stock = int(input("Minimum stock level: "))

    # Calculate expected closing stock
    expected_closing = opening + incoming - dispatched

    # Check stock discrepancy
    discrepancy = actual_closing - expected_closing

    if discrepancy == 0:
        status = "No Discrepancy"
    elif discrepancy < 0:
        status = "Stock Shortage"
    else:
        status = "Excess Stock"

    # Calculate replenishment requirement
    if actual_closing < minimum_stock:
        replenishment = minimum_stock - actual_closing
    else:
        replenishment = 0

    # Store product details
    products.append((
        name, opening, incoming, dispatched,
        expected_closing, actual_closing,
        discrepancy, status, replenishment
    ))

# Display inventory report
print("\n========== WAREHOUSE INVENTORY REPORT ==========")

for product in products:
    print("\nProduct Name:", product[0])
    print("Opening Stock:", product[1])
    print("Incoming Quantity:", product[2])
    print("Dispatched Quantity:", product[3])
    print("Expected Closing Stock:", product[4])
    print("Actual Closing Stock:", product[5])
    print("Discrepancy:", product[6])
    print("Status:", product[7])
    print("Replenishment Required:", product[8])

print("\n========== REPORT COMPLETED ==========")

