import pandas as pd

# Load the Automobile dataset
df = pd.read_csv("Automobile.csv", na_values='?')

# Display the first 5 rows
print(df.head())

# Display the entire dataset
print(df)

# Display data types of each column
print("\nData Types")
print(df.dtypes)

# Display dataset information
print("\nDataset Information")
df.info()

# Display the shape of the dataset (rows and columns)
print("\nShape of Dataset")
print(df.shape)

# Display the column names
print("\nColumn Names")
print(df.columns)

# Display statistical summary of numerical columns
print("\nStatistical Summary")
print(df.describe())

# Display the number of missing values in each column
print("\nMissing Values")
print(df.isnull().sum())