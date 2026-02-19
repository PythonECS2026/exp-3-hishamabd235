# AIM: Write a Python program to calculate the gross salary of an employee.
# Coder: Hisham Shariq Abdullah
# Date: 19/02/26

# Write your code here
bs = float(input("Enter Basic Salary: "))

da = 0.70 * bs
ta = 0.30 * bs
hra = 0.10 * bs
gross_salary = bs + da + ta + hra

print("\nSalary Details:")
print("Basic Salary:", bs)
print("DA (70%):", da)
print("TA (30%):", ta)
print("HRA (10%):", hra)
print("Gross Salary:", gross_salary)

