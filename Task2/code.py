
# Manufacturing Cost and Profitability Analysis

print("==============================================")
print("   MANUFACTURING COST AND PROFIT ANALYSIS")
print("==============================================")

# Input product details
product = input("Enter product name: ")

quantity = int(input("Enter production quantity: "))

material_per_unit = float(
    input("Enter material cost per unit: Rs. ")
)

labour_per_unit = float(
    input("Enter labour cost per unit: Rs. ")
)

wastage_percentage = float(
    input("Enter wastage percentage: ")
)

machine_cost = float(
    input("Enter machine operating cost: Rs. ")
)

selling_price = float(
    input("Enter selling price per unit: Rs. ")
)

profit_target = float(
    input("Enter expected profit target: Rs. ")
)

# Validate inputs
if (quantity <= 0 or material_per_unit < 0 or
    labour_per_unit < 0 or wastage_percentage < 0 or
    wastage_percentage > 100 or machine_cost < 0 or
    selling_price < 0 or profit_target < 0):

    print("\nInvalid Input!")
    print("Please enter valid positive values.")

else:

    # Calculate material cost
    material_cost = quantity * material_per_unit

    # Calculate labour cost
    labour_cost = quantity * labour_per_unit

    # Calculate wastage cost
    wastage_cost = material_cost * wastage_percentage / 100

    # Calculate total production cost
    total_cost = (
        material_cost + labour_cost +
        wastage_cost + machine_cost
    )

    # Calculate total revenue
    revenue = quantity * selling_price

    # Calculate profit or loss
    profit = revenue - total_cost

    # Calculate profit percentage
    if total_cost > 0:
        profit_percentage = (profit / total_cost) * 100
    else:
        profit_percentage = 0

    # Check profit target
    if profit >= profit_target:
        status = "TARGET ACHIEVED"
    else:
        status = "TARGET NOT ACHIEVED"

    # Display manufacturing report
    print("\n==============================================")
    print("       MANUFACTURING COST REPORT")
    print("==============================================")

    print("Product Name          :", product)
    print("Production Quantity   :", quantity)

    print("----------------------------------------------")
    print("              COST DETAILS")
    print("----------------------------------------------")

    print("Material Cost         : Rs.",
          round(material_cost, 2))

    print("Labour Cost           : Rs.",
          round(labour_cost, 2))

    print("Wastage Cost          : Rs.",
          round(wastage_cost, 2))

    print("Machine Cost          : Rs.",
          round(machine_cost, 2))

    print("----------------------------------------------")
    print("Total Production Cost : Rs.",
          round(total_cost, 2))

    print("Total Revenue         : Rs.",
          round(revenue, 2))

    print("Profit / Loss         : Rs.",
          round(profit, 2))

    print("Profit Percentage     :",
          round(profit_percentage, 2), "%")

    print("Expected Profit       : Rs.",
          round(profit_target, 2))

    print("----------------------------------------------")
    print("Production Status     :", status)

    print("==============================================")
    print("       ANALYSIS COMPLETED SUCCESSFULLY")
    print("==============================================")
