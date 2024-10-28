# Input employee details
employee_name = input("Enter the employee's name: ")
shifts_worked = int(input("Enter the number of shifts: "))
num_transactions = int(input("Enter the number of transactions: "))
transaction_value = float(input("Enter the transaction dollar value: "))

# Calculate productivity score
productivity_score = (transaction_value / num_transactions) / shifts_worked

# Determine bonus based on productivity score
if productivity_score <= 30:
    bonus = 50.00
elif 31 <= productivity_score <= 69:
    bonus = 75.00
elif 70 <= productivity_score <= 199:
    bonus = 100.00
else:
    bonus = 200.00

# Output employee name and bonus
print("Employee Name:", employee_name)
print("Employee Bonus: $" + str(bonus))
