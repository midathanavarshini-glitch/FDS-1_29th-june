
# Import libraries
import pandas as pd
import numpy as np
import seaborn as sns

# 1. Load the Titanic dataset
df = sns.load_dataset("titanic")

print("First five records:")
print(df.head())

print("\nDataset shape:", df.shape)

# 2. Check missing values
print("\nMissing values:")
print(df.isnull().sum())

# 3. Remove rows containing missing values
df_row_removed = df.dropna()
print("\nShape after removing null rows:", df_row_removed.shape)

# 4. Remove columns containing missing values
df_col_removed = df.dropna(axis=1)
print("\nColumns after removing null columns:")
print(df_col_removed.columns)

# 5. Fill missing numerical values with the median
df["age"] = df["age"].fillna(df["age"].median())

# 6. Fill missing categorical values with the mode
for col in ["embarked", "embark_town"]:
    df[col] = df[col].fillna(df[col].mode()[0])

print("\nMissing values after imputation:")
print(df.isnull().sum())

# 7. Check and remove duplicate rows
print("\nDuplicate rows:", df.duplicated().sum())
df = df.drop_duplicates()

# 8. Convert text values to uppercase
df["sex"] = df["sex"].str.upper()

# 9. Rename a column
df = df.rename(columns={"pclass": "Passenger_Class"})

# 10. Create a survival label
df["survival_label"] = df["survived"].map({
    0: "Not Survived",
    1: "Survived"
})

# 11. Create fare categories
df["fare_category"] = np.where(
    df["fare"] > 50, "High Fare", "Low Fare"
)

# 12. Verify the cleaned dataset
print("\nCleaned dataset:")
print(df.head())

print("\nFinal dataset shape:", df.shape)
print("\nRemaining missing values:")
print(df.isnull().sum())
