# Input statements
salary = float(input("Enter the employee's salary: "))
num_dependents = int(input("Enter the number of dependents: "))

# Calculate taxes and deductions
state_tax = salary * 0.065  # 6.5% state tax
federal_tax = salary * 0.28  # 28% federal tax
dependent_deduction = salary * 0.025 * num_dependents  # 2.5% deduction per dependent
total_withholding = state_tax + federal_tax + dependent_deduction  # total withholding
take_home_pay = salary - total_withholding  # take-home pay

# Output statements
print("State Tax: $" + str(format(state_tax, ".2f")))
print("Federal Tax: $" + str(format(federal_tax, ".2f")))
print("Dependents Deduction: $" + str(format(dependent_deduction, ".2f")))
print("Salary: $" + str(format(salary, ".2f")))
print("Take Home Pay: $" + str(format(take_home_pay, ".2f")))
