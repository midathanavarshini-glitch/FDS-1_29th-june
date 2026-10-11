
# ============================================================
# 1. DATA LOADING
# ============================================================

import pandas as pd
import numpy as np
import seaborn as sns
import sqlite3
import pickle

# Load Titanic dataset
df = sns.load_dataset("titanic")

# Display dataset
print("Complete Dataset:")
print(df)

# Print first 5 records
print("\nFirst 5 Records:")
print(df.head())

# Print last 5 rows
print("\nLast 5 Rows:")
print(df.tail())

# Print shape
print("\nDataset Shape:")
print(df.shape)

# Display information
print("\nDataset Information:")
df.info()

# Display statistical summary
print("\nStatistical Summary:")
print(df.describe())

# Display column names
print("\nColumn Names:")
print(df.columns)


# ============================================================
# 2. MISSING VALUES
# ============================================================

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Remove rows with null values
df_row_rem = df.dropna(axis=0)
print("\nRows After Removing Null Values:")
print(df_row_rem)

# Remove columns with null values
df_col_rem = df.dropna(axis=1)
print("\nColumns After Removing Null Values:")
print(df_col_rem)

# Remove rows with any null value
df_any_row = df.dropna(how="any", axis=0)
print("\nRows With No Null Values:")
print(df_any_row)

# Remove rows when all values are null
df_all_row = df.dropna(how="all", axis=0)
print("\nRows After Removing Completely Null Rows:")
print(df_all_row)

# Remove columns with any null value
df_any_col = df.dropna(how="any", axis=1)
print("\nColumns With No Null Values:")
print(df_any_col)

# Remove columns when all values are null
df_all_col = df.dropna(how="all", axis=1)
print("\nColumns After Removing Completely Null Columns:")
print(df_all_col)

# Keep rows with at least 10 non-null values
df_thresh_rows = df.dropna(thresh=10)
print("\nRows With At Least 10 Non-Null Values:")
print(df_thresh_rows)

# Keep columns with at least 500 non-null values
df_thresh_cols = df.dropna(axis=1, thresh=500)
print("\nColumns With At Least 500 Non-Null Values:")
print(df_thresh_cols)


# ============================================================
# 3. MISSING VALUE IMPUTATION
# ============================================================

# Fill Age with Mean
df_mean = df.copy()
df_mean["age"] = df_mean["age"].fillna(df_mean["age"].mean())
print("\nAge Filled With Mean:")
print(df_mean)

# Fill Age with Median
df_median = df.copy()
df_median["age"] = df_median["age"].fillna(df_median["age"].median())
print("\nAge Filled With Median:")
print(df_median)

# Fill Embarked with Mode
df_mode = df.copy()
df_mode["embarked"] = df_mode["embarked"].fillna(
    df_mode["embarked"].mode()[0]
)
print("\nEmbarked Filled With Mode:")
print(df_mode)

# Fill Age with Median and Categorical Data with Mode
df_clean = df.copy()

# Fill numerical column
df_clean["age"] = df_clean["age"].fillna(
    df_clean["age"].median()
)

# Fill categorical columns
for col in ["embarked", "embark_town"]:
    df_clean[col] = df_clean[col].fillna(
        df_clean[col].mode()[0]
    )

print("\nDataset After Imputation:")
print(df_clean)


# ============================================================
# 4. DATA CLEANING
# ============================================================

# Find duplicate rows
duplicate_count = df.duplicated().sum()
print("\nNumber of Duplicate Rows:", duplicate_count)

# Remove duplicate rows
df_no_duplicates = df.drop_duplicates()
print("\nDataset After Removing Duplicates:")
print(df_no_duplicates)

# Convert Sex to Uppercase
df["sex"] = df["sex"].astype(str).str.upper()
print("\nSex Column in Uppercase:")
print(df["sex"].head())

# Rename Column
df = df.rename(columns={"pclass": "Passenger_Class"})
print("\nDataset After Renaming Column:")
print(df.head())

# Create Survival Label
df["survival_label"] = df["survived"].map({
    0: "Not Survived",
    1: "Survived"
})
print("\nSurvival Labels:")
print(df[["survived", "survival_label"]].head())

# Create Fare Category
df["fare_category"] = np.where(
    df["fare"] > 50,
    "High Fare",
    "Low Fare"
)
print("\nFare Categories:")
print(df[["fare", "fare_category"]].head())


# ============================================================
# 5. DATA STORAGE AND FILE FORMATS
# ============================================================

# Save as CSV
df.to_csv("titanic.csv", index=False)
print("\nCSV File Created")

# Read CSV
df_csv = pd.read_csv("titanic.csv")
print("\nData Read From CSV:")
print(df_csv.head())

# Save as Text File
df_text = df[[
    "survived",
    "Passenger_Class",
    "age",
    "fare"
]]

df_text.to_csv(
    "titanic.txt",
    sep=" ",
    index=False
)
print("\nText File Created")

# Read Text File
df_text_read = pd.read_csv(
    "titanic.txt",
    sep=r"\s+"
)
print("\nData Read From Text File:")
print(df_text_read.head())

# Save as Excel
df.to_excel("titanic.xlsx", index=False)
print("\nExcel File Created")

# Read Excel
df_excel = pd.read_excel("titanic.xlsx")
print("\nData Read From Excel:")
print(df_excel.head())

# Convert Excel to CSV
df_excel.to_csv(
    "titanic_from_excel.csv",
    index=False
)
print("\nExcel Converted to CSV")


# ============================================================
# 6. BINARY DATA FORMAT
# ============================================================

# Save as Pickle
with open("titanic.pkl", "wb") as file:
    pickle.dump(df, file)

print("\nPickle Binary File Created")

# Read Pickle File
with open("titanic.pkl", "rb") as file:
    df_binary = pickle.load(file)

print("\nData Read From Pickle:")
print(df_binary.head())


# ============================================================
# 7. SQLITE DATABASE
# ============================================================

# Store Titanic Data in SQLite
conn = sqlite3.connect("titanic.db")

df.to_sql(
    "titanic_passengers",
    conn,
    if_exists="replace",
    index=False
)

print("\nData Stored in SQLite")

# Read SQL Table
df_sql = pd.read_sql_query(
    "SELECT * FROM titanic_passengers",
    conn
)

print("\nData Read From SQL Table:")
print(df_sql.head())

# Select Survived Passengers
query = """
SELECT survived, sex, age, fare
FROM titanic_passengers
WHERE survived = 1
"""

df_survived = pd.read_sql_query(query, conn)

print("\nSurvived Passengers:")
print(df_survived.head())

# Export SQL Data to CSV
df_sql.to_csv(
    "titanic_sql.csv",
    index=False
)

print("\nSQL Data Exported to CSV")

# Close Database
conn.close()
print("\nSQLite Connection Closed")


# ============================================================
# 8. COMBINING AND MERGING DATASETS
# ============================================================

# Reload Original Titanic Dataset
df_original = sns.load_dataset("titanic")

# Prepare Two DataFrames
df1 = df_original[[
    "survived",
    "pclass",
    "sex",
    "age"
]].copy()

df2 = df_original[[
    "survived",
    "fare",
    "embarked"
]].copy()

# Merge on Index
# Drop the repeated survived column from df2
merged_index = pd.merge(
    df1,
    df2.drop(columns=["survived"]),
    left_index=True,
    right_index=True
)

print("\nMerged DataFrame:")
print(merged_index.head())

print("\nMerged DataFrame Shape:")
print(merged_index.shape)


# ============================================================
# END OF PROGRAM
# ============================================================

print("\nAll Operations Completed Successfully!")
