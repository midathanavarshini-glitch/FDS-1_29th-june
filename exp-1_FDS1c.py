import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Load the dataset
url = "titanic.csv"
df = pd.read_csv(url)

sex = df['Sex']
embarked = df['Embarked']

count = 0
total = 0

for s,e in zip(sex,embarked):

    if pd.isna(s) or pd.isna(e):
        continue

    total += 1

    if s != e:
        count += 1

dissimilarity = count/total

print("\nNominal Attribute Dissimilarity")
print("Sex vs Embarked =", dissimilarity)