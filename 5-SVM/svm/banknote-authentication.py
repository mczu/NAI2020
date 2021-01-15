# Task description:
# To teach the programme classify whether banknote is authentic or not based on given features
# using classification algorithm Support Vector Machine
#
# Dataset source: https://archive.ics.uci.edu/ml/datasets/banknote+authentication
#
# Author: Magda Czubek

import pandas as pd

# Loading data
banknote_data = pd.read_csv("banknote_authentication.csv")

print(banknote_data.shape)
print(banknote_data.head())

# Data Preparation

X = banknote_data.drop('Class', axis='columns')
y = banknote_data['Class']

# Splitting data set

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y)

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




