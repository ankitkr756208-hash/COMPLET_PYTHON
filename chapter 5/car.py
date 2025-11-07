# Input vehicle type and hours
vehicle = input("Enter vehicle type (c for Car, b for Bus/Truck, s for Scooter/Cycle/Motorcycle): ").lower()
hours = int(input("Enter number of hours parked: "))

# Calculate charges
if vehicle == 'b':
    charges = 20 * hours
elif vehicle == 'c':
    charges = 10 * hours
elif vehicle == 's':
    charges = 5 * hours
else:
    charges = 0
    print("Invalid vehicle type entered!")

# Print result if valid
if charges != 0:
    print(f"Parking charges: Rs {charges}")
