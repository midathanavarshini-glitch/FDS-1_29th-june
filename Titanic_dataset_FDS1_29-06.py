import pandas as pd

# Load the dataset
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)

# Display the first 5 rows to see what the data looks like
print(df.head())
print (df)

# Get a quick overview of the data types and missing values
print(df.info())
