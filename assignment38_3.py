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

print("First five records from dataset : ")
print(df.head())

print("Last five records from dataset : ")
print(df.tail())

print("Column Names : ",list(df.columns))

print("Data types of  Column : ",df.dtypes.tolist())

print(Border)
print("total number of students: ",df.shape[0])
print(df["FinalResult"].value_counts())

print(Border)
print("Average Study hours : ",df["StudyHours"].mean())

print("Average Attendance : ",df["Attendance"].mean())

print("Maximum previous score : ",df["PreviousScore"].max())

print("Minimum Sleep Hours : ",df["SleepHours"].min())