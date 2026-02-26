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
#------------------------------------------------------------------
print(Border)
print("total number of students: ",df.shape[0])
print(df["FinalResult"].value_counts())
#-------------------------------------------------------------------
print(Border)
print("Average Study hours : ",df["StudyHours"].mean())

print("Average Attendance : ",df["Attendance"].mean())

print("Maximum previous score : ",df["PreviousScore"].max())

print("Minimum Sleep Hours : ",df["SleepHours"].min())
#-------------------------------------------------------------------
print(Border)
value=df["FinalResult"].value_counts()/df.shape[0]*100
print("Percentage of final result : ",value)

'''
students with higher study hours has most probability to pass the exam.
Students with higher attendance improves final result.
If Pass and fail counts are similar then we can say dataset is balanced.
Low study hours and less attendance can leads to fail the exam
'''

#-------------------------------------------------------------------
print(Border)
sns.histplot(data = df["StudyHours"])

plt.show()
'''
Most of the students are studying between 0 to 5 hours'''

#-------------------------------------------------------------------
print(Border)
sns.scatterplot(x=df["StudyHours"],y=df["PreviousScore"],hue=df["FinalResult"])
plt.show()

#-------------------------------------------------------------------
print(Border)
sns.boxplot(df["Attendance"])
plt.show()