# Task description:
# To teach the programme classify whether book has thick or thin cover based on given features
# using classification algorithm Support Vector Machine
#
# Features: Weight, Height, Width, Depth
# Classes: 1-thick, 0-thin
#
# Dataset author: Magda Czubek
#
# Author: Magda Czubek

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# %matplotlib inline

book_data = pd.read_csv("Books.csv")
y = book_data['Okładka']
X = book_data.drop(columns="Okładka")
sns.pairplot(book_data, hue="Okładka",palette="bright")
plt.show()

# print(book_data)
print(y.shape)
print(y.head())
print(X.shape)
print(y.head())
# Splitting data set

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20)

# Training

from sklearn.svm import SVC
model = SVC(kernel='linear')
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

# Evaluating

from sklearn.metrics import classification_report, confusion_matrix
print('Confusion matrix')
print(confusion_matrix(y_test,y_pred))
print('Classification report')
print(classification_report(y_test,y_pred))
