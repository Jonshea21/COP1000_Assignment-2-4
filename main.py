# Initialize variables
salary = float(input("Enter the employee's salary: "))  # Input for salary
numDependents = int(input("Enter the number of dependents: "))  # Input for number of dependents

# Calculate state withholding tax at 6.5%
stateTax = salary * 0.065  # 6.5 percent state tax

# Calculate federal withholding tax at 28.0%
federalTax = salary * 0.28  # 28 percent federal tax

# Calculate dependent deductions at 2.5% of the employee’s salary for each dependent
dependentDeduction = salary * 0.025 * numDependents  # 2.5 percent per dependent

# Calculate total withholding
totalWithholding = stateTax + federalTax + dependentDeduction

# Calculate take-home pay
takeHomePay = salary - totalWithholding  # Salary minus total withholding

# Output statements
print("Salary: $" + str(salary))
print("Take Home Pay: $" + str(takeHomePay))
