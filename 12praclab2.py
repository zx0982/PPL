import pandas as pd

# Sample employee data
data = {
    'Employee ID': [101, 102, 103, 104],
    'Employee Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Department': ['Automotive', 'HR', 'Automotive', 'IT'],
    'Designation': ['Developer', 'Manager', 'Tester', 'Developer']
}

df = pd.DataFrame(data)

# Create Excel file
df.to_excel("employee.xlsx", index=False)

print("employee.xlsx file created successfully!")
