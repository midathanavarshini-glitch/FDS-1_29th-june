import pandas as pd
import numpy as np

# =========================================================
# 1. CREATE DATA FRAMES
# =========================================================

students = pd.DataFrame({
    'Student_ID': [101, 102, 103, 104],
    'Name': ['Asha', 'Rahul', 'Priya', 'Arjun'],
    'Department': ['CSE', 'ECE', 'CSE', 'ECE'],
    'Marks': [85, 78, 92, 88]
})

print("STUDENT DATAFRAME")
print(students)


# =========================================================
# 2. HIERARCHICAL INDEXING
# =========================================================

data = pd.DataFrame({
    'Marks': [85, 90, 78, 88, 92, 81],
    'Attendance': [90, 95, 85, 88, 96, 89]
})

# Create hierarchical index
data.index = pd.MultiIndex.from_tuples([
    ('CSE', 101),
    ('CSE', 102),
    ('ECE', 103),
    ('ECE', 104),
    ('CSE', 105),
    ('ECE', 106)
], names=['Department', 'Student_ID'])

print("\nHIERARCHICAL INDEXING")
print(data)

# Access one department
print("\nCSE STUDENTS:")
print(data.loc['CSE'])

# Access one particular student
print("\nSTUDENT 102:")
print(data.loc[('CSE', 102)])


# =========================================================
# 3. COMBINING DATAFRAMES - CONCAT
# =========================================================

students1 = pd.DataFrame({
    'Student_ID': [101, 102],
    'Name': ['Asha', 'Rahul'],
    'Marks': [85, 78]
})

students2 = pd.DataFrame({
    'Student_ID': [103, 104],
    'Name': ['Priya', 'Arjun'],
    'Marks': [92, 88]
})

combined = pd.concat([students1, students2], ignore_index=True)

print("\nCOMBINED DATAFRAME USING CONCAT")
print(combined)


# =========================================================
# 4. CONCATENATING ALONG COLUMNS
# =========================================================

details = pd.DataFrame({
    'City': ['Hyderabad', 'Vizag', 'Chennai', 'Delhi'],
    'Age': [20, 21, 20, 22]
})

combined_columns = pd.concat(
    [students, details],
    axis=1
)

print("\nCONCATENATED ALONG COLUMNS")
print(combined_columns)


# =========================================================
# 5. MERGING DATAFRAMES
# =========================================================

student_details = pd.DataFrame({
    'Student_ID': [101, 102, 103, 104],
    'Name': ['Asha', 'Rahul', 'Priya', 'Arjun'],
    'Department': ['CSE', 'ECE', 'CSE', 'ECE']
})

student_marks = pd.DataFrame({
    'Student_ID': [101, 102, 103, 104],
    'Marks': [85, 78, 92, 88],
    'Grade': ['A', 'B', 'A+', 'A']
})

merged = pd.merge(
    student_details,
    student_marks,
    on='Student_ID'
)

print("\nMERGED DATAFRAME")
print(merged)


# =========================================================
# 6. DIFFERENT TYPES OF MERGE
# =========================================================

left_merge = pd.merge(
    student_details,
    student_marks,
    on='Student_ID',
    how='left'
)

print("\nLEFT MERGE")
print(left_merge)

right_merge = pd.merge(
    student_details,
    student_marks,
    on='Student_ID',
    how='right'
)

print("\nRIGHT MERGE")
print(right_merge)

inner_merge = pd.merge(
    student_details,
    student_marks,
    on='Student_ID',
    how='inner'
)

print("\nINNER MERGE")
print(inner_merge)

outer_merge = pd.merge(
    student_details,
    student_marks,
    on='Student_ID',
    how='outer'
)

print("\nOUTER MERGE")
print(outer_merge)


# =========================================================
# 7. MERGING ON INDEX
# =========================================================

df1 = pd.DataFrame({
    'Name': ['Asha', 'Rahul', 'Priya'],
    'Marks': [85, 78, 92]
}, index=[101, 102, 103])

df2 = pd.DataFrame({
    'Attendance': [90, 85, 96],
    'Grade': ['A', 'B', 'A+']
}, index=[101, 102, 103])

index_merge = df1.join(df2)

print("\nMERGING ON INDEX")
print(index_merge)


# =========================================================
# 8. RESHAPING USING STACK
# =========================================================

marks = pd.DataFrame({
    'Maths': [85, 78, 92],
    'Science': [90, 82, 95],
    'English': [88, 80, 91]
}, index=['Asha', 'Rahul', 'Priya'])

print("\nORIGINAL DATAFRAME")
print(marks)

stacked = marks.stack()

print("\nSTACKED DATA")
print(stacked)


# =========================================================
# 9. RESHAPING USING UNSTACK
# =========================================================

unstacked = stacked.unstack()

print("\nUNSTACKED DATA")
print(unstacked)


# =========================================================
# 10. PIVOTING - LONG TO WIDE
# =========================================================

sales = pd.DataFrame({
    'Student': ['Asha', 'Asha', 'Rahul', 'Rahul', 'Priya', 'Priya'],
    'Subject': ['Maths', 'Science', 'Maths', 'Science', 'Maths', 'Science'],
    'Marks': [85, 90, 78, 82, 92, 95]
})

print("\nLONG FORMAT")
print(sales)

pivot_data = sales.pivot(
    index='Student',
    columns='Subject',
    values='Marks'
)

print("\nPIVOTED DATA")
print(pivot_data)


# =========================================================
# 11. PIVOT TABLE
# =========================================================

sales2 = pd.DataFrame({
    'Department': ['CSE', 'CSE', 'CSE', 'ECE', 'ECE', 'ECE'],
    'Subject': ['Maths', 'Maths', 'Science',
                'Maths', 'Maths', 'Science'],
    'Marks': [85, 90, 92, 78, 82, 88]
})

pivot_table = pd.pivot_table(
    sales2,
    values='Marks',
    index='Department',
    columns='Subject',
    aggfunc='mean'
)

print("\nPIVOT TABLE")
print(pivot_table)


# =========================================================
# 12. WIDE TO LONG USING MELT
# =========================================================

wide_data = pd.DataFrame({
    'Student': ['Asha', 'Rahul', 'Priya'],
    'Maths': [85, 78, 92],
    'Science': [90, 82, 95],
    'English': [88, 80, 91]
})

print("\nWIDE FORMAT")
print(wide_data)

long_data = pd.melt(
    wide_data,
    id_vars=['Student'],
    var_name='Subject',
    value_name='Marks'
)

print("\nLONG FORMAT USING MELT")
print(long_data)


# =========================================================
# 13. SORTING HIERARCHICAL INDEX
# =========================================================

sorted_data = data.sort_index()

print("\nSORTED HIERARCHICAL INDEX")
print(sorted_data)


# =========================================================
# 14. SUMMARY STATISTICS USING GROUPBY
# =========================================================

summary = students.groupby('Department')['Marks'].mean()

print("\nAVERAGE MARKS BY DEPARTMENT")
print(summary)