import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Load the dataset
url = "titanic.csv"
df = pd.read_csv(url)

# Remove Missing Values

temp = df[['Age','Fare']].dropna()

age = temp.iloc[0]['Age']
fare = temp.iloc[0]['Fare']

age2 = temp.iloc[1]['Age']
fare2 = temp.iloc[1]['Fare']

distance = np.sqrt((age-age2)**2 + (fare-fare2)**2)

print("\nEuclidean Distance")
print(distance)

Euclidean_dissimilarity=1-(distance/100)

print("\nEuclidean Dissimilarity")
print(Euclidean_dissimilarity)
# ==========================================
# Manhattan Distance
# ==========================================

manhattan = abs(age-age2)+abs(fare-fare2)

print("\nManhattan Distance")
print(manhattan)

manhattan_dissimilarity=1-(manhattan/100)

print("\nmanhattan Dissimilarity")
print(manhattan_dissimilarity)
# ==========================================
# Minkowski Distance (p=3)
# ==========================================

minkowski=((abs(age-age2)**3)+(abs(fare-fare2)**3))**(1/3)

print("\nMinkowski Distance")
print(minkowski)

minkowski_dissimilarity=1-(minkowski/100)

print("\nminkowski Dissimilarity")
print(minkowski_dissimilarity)
# ==========================================
# Cosine Dissimilarity
# ==========================================

A=np.array([age,fare])
B=np.array([age2,fare2])

cosine_similarity=np.dot(A,B)/(np.linalg.norm(A)*np.linalg.norm(B))

print("\nCosine similarity")
print(cosine_similarity)

cosine_dissimilarity=1-cosine_similarity

print("\nCosine Dissimilarity")
print(cosine_dissimilarity)