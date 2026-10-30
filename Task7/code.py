
# Multi-Day Water Tank Simulation

capacity = float(input("Enter tank capacity: "))
initial_level = float(input("Enter initial water level: "))
threshold = float(input("Enter threshold water level: "))
days = int(input("Enter number of days: "))

# Validate initial inputs
if capacity <= 0:
    print("Tank capacity must be positive.")

elif initial_level < 0 or initial_level > capacity:
    print("Initial water level must be between 0 and tank capacity.")

elif threshold < 0 or threshold > capacity:
    print("Threshold must be between 0 and tank capacity.")

elif days <= 0:
    print("Number of days must be positive.")

else:
    current_level = initial_level
    first_threshold_day = None

    print("\n========== WATER TANK REPORT ==========")
    print("Initial Water Level:", current_level)

    for day in range(1, days + 1):

        print("\nDay", day)

        inflow = float(input("Enter water inflow: "))
        outflow = float(input("Enter water outflow: "))

        if inflow < 0 or outflow < 0:
            print("Inflow and outflow cannot be negative.")
            print("Please enter valid quantities.")
            continue

        # Calculate water level
        new_level = current_level + inflow - outflow

        # Check overflow
        if new_level > capacity:
            print("Status: Overflow Detected")
            overflow = new_level - capacity
            print("Overflow Quantity:", overflow)
            current_level = capacity

        # Check water shortage
        elif new_level < 0:
            print("Status: Water Shortage")
            shortage = abs(new_level)
            print("Shortage Quantity:", shortage)
            current_level = 0

        else:
            current_level = new_level
            print("Status: Normal")

        print("Current Water Level:", current_level)

        # Check threshold for the first time
        if (current_level >= threshold
                and first_threshold_day is None):
            first_threshold_day = day

    print("\n========== FINAL REPORT ==========")
    print("Final Water Level:", current_level)

    if first_threshold_day is not None:
        print("Threshold First Reached on Day:",
              first_threshold_day)
    else:
        print("Threshold was not reached.")

