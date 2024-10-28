# Define the list of authorized vehicles
allowed_vehicles_list = ['Ford F-150', 'Chevrolet Silverado', 'Tesla CyberTruck', 'Toyota Tundra', 'Nissan Titan']

def print_menu():
    print("********************************")
    print("AutoCountry Vehicle Finder v0.2")
    print("********************************")
    print("Please Enter the following number below from the following menu:")
    print("1. PRINT all Authorized Vehicles")
    print("2. SEARCH for Authorized Vehicle")
    print("3. Exit")

def print_vehicles():
    print("The AutoCountry sales manager has authorized the purchase and selling of the following vehicles:")
    for vehicle in allowed_vehicles_list:
        print(vehicle)

def search_vehicle(vehicle_name):
    # Check if the entered vehicle name is in the list of authorized vehicles
    if vehicle_name in allowed_vehicles_list:
        return f"{vehicle_name} is an authorized vehicle."
    else:
        return f"{vehicle_name} is not an authorized vehicle; if you received this in error please check the spelling and try again."

def main():
    while True:
        print_menu()
        choice = input("Enter your choice: ")
        
        if choice == "1":
            print_vehicles()
        elif choice == "2":
            vehicle_name = input("Please Enter the full Vehicle name: ")
            result = search_vehicle(vehicle_name)
            print(result)
        elif choice == "3":
            print("Thank you for using the AutoCountry Vehicle Finder, good-bye!")
            break
        else:
            print("Invalid input. Please select 1, 2, or 3.")

# Start the program
if __name__ == "__main__":
    main()
