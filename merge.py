import pandas as pd

# Employee DataFrame
employee = pd.DataFrame({
    'Emp_ID': [101, 102, 103, 104],
    'Name': ['John', 'Alice', 'Bob', 'David'],
    'Dept': ['HR', 'IT', 'Finance', 'Marketing']
})

# Salary DataFrame
salary = pd.DataFrame({
    'Emp_ID': [101, 102, 103, 105],
    'Designation': ['Manager', 'Developer', 'Analyst', 'Tester'],
    'Salary': [60000, 50000, 45000, 40000]
})
# emp1 DataFrame
emp1 = pd.DataFrame({
    'Emp_ID': [104, 105, 106],
    'Name': ['David', 'Eva', 'Frank'],
    'Dept': ['Marketing', 'HR', 'IT']
})
print("Employee DataFrame")
print(employee)

print("\nSalary DataFrame")
print(salary)

#normal merge
normal_merge = pd.merge(employee, salary, on='Emp_ID')
print(normal_merge)

#merge=inner
inner_merge = pd.merge(employee, salary, on='Emp_ID', how='inner')
print(inner_merge)

#merge=outer
outer_merge = pd.merge(employee, salary, on='Emp_ID', how='outer')
print(outer_merge)

#merge=left
left_merge = pd.merge(employee, salary, on='Emp_ID', how='left')
print(left_merge)

#merge=right
right_merge = pd.merge(employee, salary, on='Emp_ID', how='right')
print(right_merge)

#concadination=row
concat_rows = pd.concat([employee, salary], axis=0)
print(concat_rows)

#concadinatio=column
concat_cols = pd.concat([employee, salary], axis=1)
print(concat_cols)

#concat on rows of emp and emp1 =vertical
concat_rows = pd.concat([emp, emp1], axis=0)
print(concat_rows)

#concat on columns of emp and emp1 =horizontal
concat_cols = pd.concat([emp, emp1], axis=1)
print(concat_cols)

#merge a outer merge result with new emp1
concat_cols = pd.concat([outer_merge, emp1], axis=1)
print("\nColumn-wise Concatenation")
print(concat_cols)

#merge a outer merge result with new emp1
concat_rows = pd.concat([outer_merge, emp1], axis=0)
print("\nRow-wise Concatenation")
print(concat_rows)

# Filter rows where Name is HP
filtered_data = outer_merge[outer_merge['Name'] == 'HP']
print(filtered_data)
#or
filtered_data = outer_merge[outer_merge== 'HP'].name
print(filtered_data)

#using and
result_and = outer_merge[
    (outer_merge['Dept'] == 'HR') &
    (outer_merge['Salary'] > 50000)
]
print(result_and)

#using or
result_or = outer_merge[
    (outer_merge['Dept'] == 'HR') |
    (outer_merge['Salary'] > 50000)
]
print(result_or)

#using between
result_between = outer_merge[
    outer_merge['Salary'].between(45000, 60000)
]
print(result_between)