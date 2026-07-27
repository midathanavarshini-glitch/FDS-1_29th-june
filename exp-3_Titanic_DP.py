# ==========================================
# Data Preprocessing on Titanic Dataset
# ==========================================

import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler

# ------------------------------------------
# Step 1: Read the Dataset
# ------------------------------------------

df = pd.read_csv("titanic.csv")

print("First Five Records")
print(df.head())

print("\nDataset Shape:", df.shape)

print("\nData Types")
print(df.dtypes)

# ------------------------------------------
# Step 2: Check Missing Values
# ------------------------------------------

print("\nMissing Values")
print(df.isnull().sum())

# ------------------------------------------
# Step 3: Handle Missing Values
# ------------------------------------------

# Fill Age with Mean
df['Age'] = df['Age'].fillna(df['Age'].mean())

# Fill Embarked with Mode
df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])

# Fill Cabin with "Unknown"
df['Cabin'] = df['Cabin'].fillna("Unknown")

print("\nMissing Values After Imputation")
print(df.isnull().sum())

# ------------------------------------------
# Step 4: Remove Duplicate Records
# ------------------------------------------

print("\nDuplicate Records:", df.duplicated().sum())

df = df.drop_duplicates()

print("Dataset Shape After Removing Duplicates:", df.shape)

# ------------------------------------------
# Step 5: Encode Categorical Variables
# ------------------------------------------

encoder = LabelEncoder()

df['Sex'] = encoder.fit_transform(df['Sex'])

df['Embarked'] = encoder.fit_transform(df['Embarked'])

print("\nEncoded Data")
print(df[['Sex','Embarked']].head())

# ------------------------------------------
# Step 6: Feature Scaling
# ------------------------------------------

scaler = StandardScaler()

df[['Age','Fare']] = scaler.fit_transform(df[['Age','Fare']])

print("\nStandardized Age and Fare")
print(df[['Age','Fare']].head())

# ------------------------------------------
# Step 7: Min-Max Normalization
# ------------------------------------------

normalizer = MinMaxScaler()

df[['Age','Fare']] = normalizer.fit_transform(df[['Age','Fare']])

print("\nNormalized Age and Fare")
print(df[['Age','Fare']].head())

# ------------------------------------------
# Step 8: Detect Outliers
# ------------------------------------------

Q1 = df['Fare'].quantile(0.25)
Q3 = df['Fare'].quantile(0.75)

IQR = Q3 - Q1

Lower = Q1 - 1.5 * IQR
Upper = Q3 + 1.5 * IQR

outliers = df[(df['Fare'] < Lower) | (df['Fare'] > Upper)]

print("\nNumber of Outliers in Fare:", len(outliers))

# ------------------------------------------
# Step 9: Remove Outliers
# ------------------------------------------

df = df[(df['Fare'] >= Lower) & (df['Fare'] <= Upper)]

print("Dataset Shape After Removing Outliers")
print(df.shape)

# ------------------------------------------
# Step 10: Drop Unnecessary Columns
# ------------------------------------------

df = df.drop(['PassengerId','Name','Ticket','Cabin'], axis=1)

print("\nFinal Dataset")
print(df.head())

# ------------------------------------------
# Step 11: Save Preprocessed Dataset
# ------------------------------------------

df.to_csv("Titanic_Preprocessed.csv", index=False)

print("\nPreprocessed dataset saved successfully.")
