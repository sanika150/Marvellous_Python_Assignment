from turtle import distance

import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier

from sklearn.ensemble import VotingClassifier
from sklearn.metrics import accuracy_score,confusion_matrix,classification_report,ConfusionMatrixDisplay
import matplotlib.pyplot as plt
import seaborn as sns


# Load your data into a DataFrame (example with a hypothetical 'df' and 'target_variable')
# df = pd.read_csv('your_data.csv')


def main():
    Border = "-" *50
    print(Border)
    df =pd.read_csv("diabetes.csv")

    print("First 5 records from dataset are :",df.head())

    print("check for null values in dataset :",df.isnull().sum())
    print(Border)
    print("Description of dataset is :",df.describe())
    print(Border)
    plt.figure(figsize=(8, 6))
    sns.countplot(x='Outcome', data=df)
    plt.title('Distribution of Target Variable (Categorical)')
    plt.xlabel('Category')
    plt.ylabel('Count')
    plt.show()

    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(df.drop('Outcome',axis = 1))

    X = scaled_data
    Y = df['Outcome']

    X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size =0.2,random_state=42)

    modellr = LogisticRegression(max_iter=5000)
    modeldt = DecisionTreeClassifier(random_state=42)

    modellr.fit(X_train,Y_train)
    modeldt.fit(X_train,Y_train)

    hard_model = VotingClassifier(
        estimators=[
            ('lr',modellr),
            ('dt',modeldt)
        ],
        voting='hard'
    )

    hard_model.fit(X_train,Y_train)

    pred_hard = hard_model.predict(X_test)
    acc_hard = accuracy_score(pred_hard,Y_test)
    print(Border)
    print("Hard voting accuracy : ",acc_hard)
    print(Border)
    cm = confusion_matrix(Y_test,pred_hard,labels=hard_model.classes_)
    print(cm)
    graph = ConfusionMatrixDisplay(confusion_matrix=cm,display_labels=hard_model.classes_)
    graph.plot()
    plt.show()
    print(Border)
    print("Classification Report : ")
    print(classification_report(Y_test,pred_hard))
    print(Border)
    print(Border)

    output = pd.DataFrame({
        'Actual': Y_test,
        'Predicted': pred_hard
    })
    output.to_csv('Diabetes _prediction.csv',index = False)

    print("Output saved to 'Diabetes_prediction.csv' successfully")
  

if __name__ == "__main__":
    main()