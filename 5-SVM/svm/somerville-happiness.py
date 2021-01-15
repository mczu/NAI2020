# Task description:
# To teach the programme classify whether citizen is happy(1) or unhappy(0) based on given attributes
# using classification algorithm Support Vector Machine
# Dataset source: http://archive.ics.uci.edu/ml/datasets/Somerville+Happiness+Survey

# Attribute Information provided by data set authors:
# D = decision attribute (D) with values 0 (unhappy) and 1 (happy)
# X1 = the availability of information about the city services
# X2 = the cost of housing
# X3 = the overall quality of public schools
# X4 = your trust in the local police
# X5 = the maintenance of streets and sidewalks
# X6 = the availability of social community events
# Attributes X1 to X6 have values 1 to 5.

# Author: Magda Czubek

import pandas as pd

# Loading data
happiness_data = pd.read_csv("SomervilleHappinessSurvey.csv")

# Data Preparation
X = happiness_data.drop('D', axis='columns')
y = happiness_data['D']

# Splitting data set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.40)

# Training the Algorithm

from sklearn.svm import SVC
model = SVC(kernel='linear')
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

# Evaluating the Algorithm

from sklearn.metrics import classification_report, confusion_matrix
print('Confusion matrix')
print(confusion_matrix(y_test,y_pred))
print('Classification report')
print(classification_report(y_test,y_pred))
