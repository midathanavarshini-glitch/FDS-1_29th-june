import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("Automobile.csv")

# 1. Price Distribution
plt.figure(figsize=(6,4))
sns.histplot(df['price'], bins=20, kde=True)
plt.title("Price Distribution")
plt.show()

# 2. Fuel Type Distribution
plt.figure(figsize=(6,4))
sns.countplot(x='fuel-type', data=df)
plt.title("Fuel Type Distribution")
plt.show()

# 3. Body Style Distribution
plt.figure(figsize=(8,5))
sns.countplot(x='body-style', data=df)
plt.title("Body Style Distribution")
plt.show()

# 4. Engine Size vs Price
plt.figure(figsize=(6,4))
sns.scatterplot(x='engine-size', y='price', data=df)
plt.title("Engine Size vs Price")
plt.show()

# 5. Fuel Type vs Price
plt.figure(figsize=(6,4))
sns.boxplot(x='fuel-type', y='price', data=df)
plt.title("Fuel Type vs Price")
plt.show()

# 6. Correlation Heatmap
plt.figure(figsize=(12,8))
sns.heatmap(df.corr(numeric_only=True),
            annot=True,
            cmap='coolwarm')
plt.title("Correlation Matrix")
plt.show()