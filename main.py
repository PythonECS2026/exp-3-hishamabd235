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
print(f"Basic Salary:  {bs}")
print(f"DA (70%):      {da}")
print(f"TA (30%):      {ta}")
print(f"HRA (10%):     {hra}")
print(f"Gross Salary:  {gross_salary}")
