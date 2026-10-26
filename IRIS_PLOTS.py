import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

# Load Iris Dataset
iris = load_iris()

df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['species'] = iris.target
df['species'] = df['species'].map({
    0: 'setosa',
    1: 'versicolor',
    2: 'virginica'
})

print(df.head())

# ---------------------------
# 1. Scatter Plot
# ---------------------------
plt.figure(figsize=(8,6))
sns.scatterplot(
    data=df,
    x='sepal length (cm)',
    y='sepal width (cm)',
    hue='species'
)
plt.title("Sepal Length vs Sepal Width")
plt.show()

# ---------------------------
# 2. Histogram
# ---------------------------
plt.figure(figsize=(8,6))
sns.histplot(
    df['petal length (cm)'],
    bins=15,
    kde=True,
    color='green'
)
plt.title("Distribution of Petal Length")
plt.show()

# ---------------------------
# 3. Box Plot
# ---------------------------
plt.figure(figsize=(8,6))
sns.boxplot(
    x='species',
    y='petal width (cm)',
    data=df
)
plt.title("Petal Width by Species")
plt.show()

# ---------------------------
# 4. Pair Plot
# ---------------------------
sns.pairplot(df, hue='species')
plt.show()

# ---------------------------
# 5. Heatmap (Correlation)
# ---------------------------
plt.figure(figsize=(8,6))
numeric_df = df.drop('species', axis=1)

sns.heatmap(
    numeric_df.corr(),
    annot=True,
    cmap='coolwarm'
)

plt.title("Correlation Heatmap")
plt.show()

# ---------------------------
# 6. Violin Plot
# ---------------------------
plt.figure(figsize=(8,6))
sns.violinplot(
    x='species',
    y='sepal length (cm)',
    data=df
)
plt.title("Sepal Length Distribution")
plt.show()

# ---------------------------
# 7. Count Plot
# ---------------------------
plt.figure(figsize=(8,6))
sns.countplot(
    x='species',
    data=df,
    palette='Set2'
)
plt.title("Species Count")
plt.show()

# ---------------------------
# 8. Line Plot
# ---------------------------
plt.figure(figsize=(10,6))
plt.plot(
    df.index,
    df['sepal length (cm)'],
    color='red'
)
plt.title("Sepal Length Trend")
plt.xlabel("Index")
plt.ylabel("Sepal Length")
plt.show()