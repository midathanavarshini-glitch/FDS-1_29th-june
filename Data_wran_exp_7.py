import pandas as pd

# Employee DataFrame
employee = pd.DataFrame({
    'Emp_ID': [101, 102, 103, 104],
    'Emp_Name': ['John', 'Alice', 'Bob', 'Emma'],
    'Department': ['HR', 'IT', 'Finance', 'Sales']
})

# Salary DataFrame
salary = pd.DataFrame({
    'Emp_ID': [101, 102, 103, 105],
    'Salary': [50000, 60000, 55000, 70000]
})

print("Employee DataFrame")
print(employee)

print("\nSalary DataFrame")
print(salary)

# merge = inner
inner_merge = pd.merge(employee, salary, on='Emp_ID', how='inner')
print("\nInner Merge")
print(inner_merge)

# merge = outer
outer_merge = pd.merge(employee, salary, on='Emp_ID', how='outer')
print("\nOuter Merge")
print(outer_merge)

# merge = left
left_merge = pd.merge(employee, salary, on='Emp_ID', how='left')
print("\nLeft Merge")
print(left_merge)

# merge = right
right_merge = pd.merge(employee, salary, on='Emp_ID', how='right')
print("\nRight Merge")
print(right_merge)

# concatenation = row
concat_rows = pd.concat([employee, salary], axis=0)
print("\nRow Concatenation")
print(concat_rows)

# concatenation = column
concat_cols = pd.concat([employee, salary], axis=1)
print("\nColumn Concatenation")
print(concat_cols)