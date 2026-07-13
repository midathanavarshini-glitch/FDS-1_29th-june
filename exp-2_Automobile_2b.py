import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("Automobile.csv")

# ==========================================
# Identify Various Attribute Types
# ==========================================

# Numeric Attributes
print("\nNumeric Attributes")
numeric = df.select_dtypes(include=['int64', 'float64']).columns
print(numeric)

# Nominal Attributes
print("\nNominal Attributes")
nominal = ['make', 'fuel-type', 'aspiration', 'body-style',
           'drive-wheels', 'engine-location', 'engine-type',
           'num-of-cylinders', 'fuel-system']
print(nominal)

# Binary Attributes
print("\nBinary Attributes")
binary = ['fuel-type', 'aspiration', 'engine-location']
print(binary)