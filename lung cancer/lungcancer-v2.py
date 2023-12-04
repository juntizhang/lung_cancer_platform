# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 14:20:26 2023

@author: zzzzzm
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from imblearn.over_sampling import SMOTE
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix

# Load the dataset
df = pd.read_csv("survey lung cancer.csv", index_col=None)
df.head()
df.info()
df.isnull().sum()
# Data preprocessing
df.GENDER.replace({"M": 1, "F": 0}, inplace=True)
df.LUNG_CANCER.replace({"YES": 1, "NO": 0}, inplace=True)

# Visualize data
figure, axes = plt.subplots(nrows=4, ncols=4, figsize=(20, 16))
i = 0
for column in df.columns:
    x = int(i / 4)
    y = i % 4
    df[column].value_counts().plot(ax=axes[x][y], kind='bar', title=f"{column} scatter gram")
    i = i + 1

smoke_yes = df.loc[df.SMOKING == 2, ["SMOKING", "LUNG_CANCER"]]
smoke_no = df.loc[df.SMOKING == 1, ["SMOKING", "LUNG_CANCER"]]

fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(16, 8))
ax1.pie(smoke_yes.LUNG_CANCER.value_counts(normalize=True), labels=["YES", "NO"], colors=["yellow", "green"], autopct='%1.1f%%', shadow=True)
ax1.set_title("Lung Cancer & Smoking_YES")
ax2.pie(smoke_no.LUNG_CANCER.value_counts(normalize=True), labels=["YES", "NO"], colors=["red", "green"], autopct='%1.1f%%', shadow=True)
ax2.set_title("Lung Cancer & Smoking_NO")

fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(30, 8))
sns.countplot(x=df.LUNG_CANCER, hue=df["ALLERGY "], ax=ax1, palette=['green', 'black'])
sns.countplot(x=df.LUNG_CANCER, hue=df.COUGHING, ax=ax2, palette=['green', 'black'])
sns.countplot(x=df.LUNG_CANCER, hue=df["ALCOHOL CONSUMING"], ax=ax3, palette=['green', 'black'])

fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(30, 8))
sns.countplot(x=df.LUNG_CANCER, hue=df["SWALLOWING DIFFICULTY"], ax=ax1, palette=['green', 'black'])
sns.countplot(x=df.LUNG_CANCER, hue=df.WHEEZING, ax=ax2, palette=['green', 'black'])
sns.countplot(x=df.LUNG_CANCER, hue=df["CHEST PAIN"], ax=ax3, palette=['green', 'black'])

plt.figure(figsize=(16, 10))
sns.heatmap(df.corr(), annot=True, cmap='viridis', vmin=0, vmax=1)

# SMOTE for balancing the data
X = df.drop(columns=["LUNG_CANCER"], axis=1)
y = df["LUNG_CANCER"]

smote = SMOTE(sampling_strategy='minority')
X, y = smote.fit_resample(X, y)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=2023)

# Standardize the data
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Train a Random Forest Classifier
rf = RandomForestClassifier()
rf.fit(X_train, y_train)
y_prdrf = rf.predict(X_test)

# Evaluate the model
print(classification_report(y_test, y_prdrf))
cvs_rf = round(cross_val_score(rf, X, y, scoring="accuracy", cv=10).mean(), 2)
print("Cross validation score for Random Forest Classifier model is:", cvs_rf)

# Visualize the confusion matrix
sns.heatmap(confusion_matrix(y_test, y_prdrf), annot=True, cmap='viridis')
plt.xlabel("Predicted")
plt.ylabel("Truth")
plt.title("Confusion matrix - Random Forest Classifier")

plt.show()
