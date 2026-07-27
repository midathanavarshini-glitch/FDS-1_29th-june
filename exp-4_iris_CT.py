# ==========================================
# Measures of Central Tendency - Iris Dataset
# ==========================================

import pandas as pd

# Load the Iris dataset
df = pd.read_csv("iris.csv")

# Display first 5 rows
print("First 5 Rows:")
print(df.head())

# ==========================================
# Check for Null Values
# ==========================================

print("\nMissing Values:")
print(df.isnull().sum())

# ==========================================
# Mean
# ==========================================

print("\nMean:")
print(df.mean(numeric_only=True))

# ==========================================
# Median
# ==========================================

print("\nMedian:")
print(df.median(numeric_only=True))

# ==========================================
# Mode
# ==========================================

print("\nMode:")
print(df.mode())