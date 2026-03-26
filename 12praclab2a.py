import pandas as pd

# Read the Excel file (keep employee.xlsx in same folder)
df = pd.read_excel("employee.xlsx")

# a) Print list of employees working for "Automotive" domain
print("Employees in Automotive Domain:\n")
auto_emp = df[df['Department'] == 'Automotive']
print(auto_emp)

# b) Print details of an employee using Employee ID
emp_id = int(input("\nEnter Employee ID: "))
emp_details = df[df['Employee ID'] == emp_id]

if not emp_details.empty:
    print("\nEmployee Details:\n")
    print(emp_details)
else:
    print("\nEmployee not found!")

# d) Print list of all Developers
print("\nList of Developers:\n")
developers = df[df['Designation'] == 'Developer']
print(developers)
