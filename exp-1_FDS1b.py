import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Load the dataset
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

print(binary)