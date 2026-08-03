import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

"""# Load the dataset
url = "titanic.csv"
df = pd.read_csv(url)

print("\nNumeric Attributes")
numeric = df.select_dtypes(include=['int64','float64']).columns
print(numeric)

print("\nNominal Attributes")
nominal = ['Sex','Embarked']

print(nominal)

print("\nBinary Attributes")
binary = ['Survived']

print(binary)"""

# Load Titanic dataset
df = pd.read_csv("titanic.csv")

# Identify numeric attributes
numeric = df.select_dtypes(include=['int64','float64']).columns.tolist()

# Identify binary attributes (numeric with only 2 unique values)
binary = [col for col in numeric if df[col].nunique() == 2]

# Remaining numeric attributes (excluding binary)
numeric = [col for col in numeric if col not in binary]

# Identify nominal attributes (object or category dtype)
nominal = df.select_dtypes(include=['object','category']).columns.tolist()

print("\nNumeric Attributes:", numeric)
print("\nNominal Attributes:", nominal)
print("\nBinary Attributes:", binary)
