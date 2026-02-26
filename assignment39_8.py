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
df = pd.read_csv(DatasetPath)
#store csv data in df
###########################################################
#Step 2: Data Analysis(EDA)
###########################################################
print(Border)
print("Step 2 : Data Analysis")
print(Border)

print("Shape of dataset : ",df.shape)
#list of column
print("Column Names : ",list(df.columns))
print("Missing values (Per column)")
print(df.isnull().sum())



print("Statistical report of dataset :")
print(df.describe())

###########################################################
#Step 3: Decide independent and dependent vatiables
###########################################################
print(Border)

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
###########################################################
#Step 4: Visualization of the dataset
###########################################################
print(Border)
print("Step 4 : Visualization of the dataset")
print(Border)

#Scatter plot
plt.figure(figsize=(7,5))

sns.barplot(x="FinalResult", y="StudyHours", hue="Attendance", data=df)

plt.title("Final Result vs Study Hours (Grouped by Attendance)")

plt.xlabel("Final Result")
plt.ylabel("Study Hours")
plt.legend()
plt.grid(True)
plt.show()
###########################################################
#Step 5: Split the dataset for training and testing
###########################################################
print(Border)
print("Step 5 : Split the dataset for training and testing")
print(Border)

#Test size = 20%
#Train size = 80%
print("X_train : ",X_train.shape) 
print("X_test : ",X_test.shape) 

print("Y_train : ",Y_train.shape) 
print("Y_test : ",Y_test.shape)
#---------------------------------------------------------
###########################################################
#Step 6: Build the model
###########################################################
print(Border)
print("Step 6 : Build the model")
print(Border)

model = DecisionTreeClassifier(
    criterion="gini",
    max_depth= 5, #tunning tunned value
    random_state= 42
)
###########################################################
#Step 7: Train the model
###########################################################
print(Border)
print("Step 7 : Train the model")
print(Border)
model.fit(X_train,Y_train)

print("Model training completed")
#---------------------------------------------------------
###########################################################
#Step 8: Evaluate the model
###########################################################
print(Border)
print("Step 8 : Evaluate the model")
print(Border)
Y_pred = model.predict(X_test)

print("Model Evaluation (Testing) complete")

print(Y_pred.shape)

print("Expected answers : ")
print(list[Y_test])

print("Ptredicted answers : ")
print(Y_pred)
#---------------------------------------------------------
###########################################################
#Step 9: Evaluate the model performance
###########################################################
print(Border)
print("Step 9 : Evaluate the model performance")
print(Border)
accuracy = accuracy_score(Y_test,Y_pred)

print("Accuracy of model is : ",accuracy * 100)
#---------------------------------------------------------
print(Border)
cm = confusion_matrix(Y_test,Y_pred)

print("Confusion matrix : ")
print(cm)

#---------------------------------------------------------
###########################################################
#Step 10: Plot confusion matrix
###########################################################
print(Border)
print("Step 10 : Plot confusion matrix")
print(Border)


data = ConfusionMatrixDisplay(confusion_matrix=cm,display_labels=model.classes_)

data.plot()
plt.title("Confusion matrix of Iris dataset")
plt.show()