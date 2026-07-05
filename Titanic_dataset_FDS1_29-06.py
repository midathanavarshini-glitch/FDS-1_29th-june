import pandas as pd

# Load the dataset
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)

# Display the first 5 rows
print(df.head())

# Display the entire dataset
print(df)

# Display dataset information
print(df.info())

# Display the shape of the dataset (rows and columns)
print(df.shape)

# Display the column names
print(df.columns)

# Display statistical summary of numerical columns
print(df.describe())

# Display the number of missing values in each column
print(df.isnull().sum())
