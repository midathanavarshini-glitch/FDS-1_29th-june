# ==========================================
# Measures of Dispersion - Titanic Dataset
# ==========================================

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv("titanic.csv")

# ------------------------------------------
# Display first 5 rows
# ------------------------------------------

print("First Five Records")
print(df.head())

# ------------------------------------------
# Check Missing Values
# ------------------------------------------

print("\nMissing Values")
print(df.isnull().sum())

# Fill missing values in Age
df['Age'] = df['Age'].fillna(df['Age'].mean())

# ------------------------------------------
# Measures of Dispersion
# ------------------------------------------

print("\nVariance")
print(df[['Age','Fare']].var())

print("\nStandard Deviation")
print(df[['Age','Fare']].std())

print("\nRange")
print(df[['Age','Fare']].max() - df[['Age','Fare']].min())

print("\nInterquartile Range (IQR)")

Q1 = df[['Age','Fare']].quantile(0.25)
Q3 = df[['Age','Fare']].quantile(0.75)

IQR = Q3 - Q1

print(IQR)

# ------------------------------------------
# Histogram
# ------------------------------------------

plt.figure(figsize=(6,4))
sns.histplot(df['Age'], bins=20, kde=True)

plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")

plt.show()

# ------------------------------------------
# Box Plot
# ------------------------------------------

plt.figure(figsize=(6,4))
sns.boxplot(y=df['Fare'])

plt.title("Fare Box Plot")

plt.show()

# ------------------------------------------
# Density Plot
# ------------------------------------------

plt.figure(figsize=(6,4))
sns.kdeplot(df['Age'], fill=True)

plt.title("Age Density Curve")

plt.show()