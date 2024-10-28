# CarFinder v0.1

# List of allowed vehicles
AllowedVehiclesList = ['Ford F-150', 'Chevrolet Silverado', 'Tesla CyberTruck', 
                       'Toyota Tundra', 'Nissan Titan']

def print_menu():
    """Displays the main menu."""
    print("\n********************************")
    print("AutoCountry Vehicle Finder v0.1")
    print("********************************")
    print("Please Enter the following number below from the following menu:\n")
    print("1. PRINT all Authorized Vehicles")
    print("2. Exit")

def print_vehicles():
    """Prints the list of authorized vehicles."""
    print("\nThe AutoCountry sales manager has authorized the purchase and selling of the following vehicles:")
    for vehicle in AllowedVehiclesList:
        print(vehicle)

def main():
    """Main function to run the CarFinder program."""
    while True:
        print_menu()  # Display the menu
        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            print_vehicles()
        elif choice == "2":
            print("\nThank you for using the AutoCountry Vehicle Finder, good-bye!")
            break
        else:
            print("\nInvalid input. Please select 1 or 2.")

# Run the program
if __name__ == "__main__":
    main()
