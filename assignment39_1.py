import pandas as pd

import matplotlib.pyplot as plt

import seaborn as sns

from sklearn.model_selection import train_test_split

from sklearn.tree import DecisionTreeClassifier,plot_tree

from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report,
    ConfusionMatrixDisplay
)

Border = "-"*100
###########################################################
#Step 1: Load the dataset
###########################################################
print(Border)
print("Step 1 : load the dataset")
print(Border)

DatasetPath = "student_performance_ml.csv"
#store csv data in df
df = pd.read_csv(DatasetPath)
feature_cols = [
    "StudyHours",
    "Attendance",
    "PreviousScore",
    "AssignmentsCompleted",
    "SleepHours"
]

X = df[feature_cols]
Y = df["FinalResult"]
X_train,X_test,Y_train,Y_test = train_test_split(
    X,
    Y,
    test_size=0.5,
    random_state=42
)
print("Data splitting activity done : ")

print("X - Independent : ",X.shape) 
print("Y - Dependent : ",Y.shape)

print("X_train : ",X_train.shape) 
print("X_test : ",X_test.shape) 

print("Y_train : ",Y_train.shape) 
print("Y_test : ",Y_test.shape)
#---------------------------------------------------------
print(Border)
model = DecisionTreeClassifier(
    criterion="gini",
    max_depth= 5, #tunning tunned value
    random_state= 42
)
model.fit(X_train,Y_train)

print("Model training completed")