import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("Automobile.csv")

# ==========================================
# Identify Various Attribute Types
# ==========================================

import pandas as pd

# Load dataset
df = pd.read_csv("automobile.csv")

# Numeric attributes
numeric = df.select_dtypes(include=['int64','float64']).columns.tolist()

# Binary attributes (columns with exactly 2 unique values)
binary = [col for col in df.columns if df[col].nunique() == 2]

# Exclude binary from numeric
numeric = [col for col in numeric if col not in binary]

# Nominal attributes (object/category dtype)
nominal = df.select_dtypes(include=['object','category']).columns.tolist()

print("\nNumeric Attributes:", numeric)
print("\nNominal Attributes:", nominal)
print("\nBinary Attributes:", binary)
