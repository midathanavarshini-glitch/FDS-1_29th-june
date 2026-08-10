import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load Iris dataset
df = sns.load_dataset("iris")

# Display first 5 rows
print(df.head())

# Calculate correlation
correlation = df.select_dtypes("number").corr()

print(correlation)

# Plot correlation heatmap
sns.heatmap(correlation, annot=True, cmap="coolwarm")
plt.title("Correlation Plot of Iris Dataset")
plt.show()