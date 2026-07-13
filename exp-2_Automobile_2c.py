import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("Automobile.csv")
# ==========================================
# Nominal Attribute Dissimilarity
# ==========================================

fuel = df['fuel-type']
aspiration = df['aspiration']

count = 0
total = 0

for f, a in zip(fuel, aspiration):

    if pd.isna(f) or pd.isna(a):
        continue

    total += 1

    if f != a:
        count += 1

dissimilarity = count / total

print("\nNominal Attribute Dissimilarity")
print("Fuel Type vs Aspiration =", dissimilarity)