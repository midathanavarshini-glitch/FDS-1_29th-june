# ==========================================
# Similarity and Dissimilarity Measures
# Automobile Dataset
# ==========================================

import numpy as np
import pandas as pd

# Load the Automobile dataset
df = pd.read_csv("Automobile.csv", na_values='?')

temp = df[['engine-size', 'price']].dropna()

# First automobile
engine1 = temp.iloc[0]['engine-size']
price1 = temp.iloc[0]['price']

# Second automobile
engine2 = temp.iloc[1]['engine-size']
price2 = temp.iloc[1]['price']

# ==========================================
# Euclidean Distance
# ==========================================

euclidean = np.sqrt((engine1-engine2)**2 + (price1-price2)**2)

print("\nEuclidean Distance")
print(euclidean)

Euclidean_dissimilarity=1-(euclidean/100)

print("\nEuclidean Dissimilarity")
print(Euclidean_dissimilarity)

# ==========================================
# Manhattan Distance
# ==========================================

manhattan = abs(engine1-engine2) + abs(price1-price2)

print("\nManhattan Distance")
print(manhattan)

manhattan_dissimilarity=1-(manhattan/100)

print("\nmanhattan Dissimilarity")
print(manhattan_dissimilarity)
# ==========================================
# Minkowski Distance (p = 3)
# ==========================================

minkowski = ((abs(engine1-engine2)**3) + (abs(price1-price2)**3))**(1/3)

print("\nMinkowski Distance")
print(minkowski)

minkowski_dissimilarity=1-(minkowski/100)

print("\nminkowski Dissimilarity")
print(minkowski_dissimilarity)
# ==========================================
# Cosine Similarity
# ==========================================

A = np.array([engine1, price1])
B = np.array([engine2, price2])

cosine_similarity = np.dot(A, B) / (np.linalg.norm(A) * np.linalg.norm(B))

print("\nCosine Similarity")
print(cosine_similarity)

# ==========================================
# Cosine Dissimilarity
# ==========================================

cosine_dissimilarity = 1 - cosine_similarity

print("\nCosine Dissimilarity")
print(cosine_dissimilarity)