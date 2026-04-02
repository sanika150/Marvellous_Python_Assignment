from turtle import distance

import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import VotingClassifier
from sklearn.metrics import accuracy_score,confusion_matrix,classification_report,ConfusionMatrixDisplay
import matplotlib.pyplot as plt
import seaborn as sns


# Load your data into a DataFrame (example with a hypothetical 'df' and 'target_variable')
# df = pd.read_csv('your_data.csv')


def main():
    Border = "-" *50
    print(Border)
    df =pd.read_csv("bank-full.csv")
    print("First 5 records from dataset are :",df.head())

    print("check for null values in dataset :",df.isnull().sum())
    print(Border)
    print("Description of dataset is :",df.describe())
    print(Border)

   
    #df= df.drop('duration',axis=1)

    for col in df.columns:
        if df[col].dtype == 'object':
            df[col]=df[col].replace('unknown',df[col].mode()[0])

    sns.countplot(X='y',data=df)
    plt.title("Class Distribution")
    plt.show()

    

    print(Border)

    encoder = LabelEncoder()

    for col in df.columns:
        if df[col].dtype == 'object':
            df[col] = encoder.fit_transform(df[col])

    print(df.head())

    df.columns = df.columns.str.strip()
    
    print(df.columns)
    print(Border)

    #X = df['age','job','marital','education','default','balance','housing','loan','contact','day','month','duration','campaign','pdays','previous','poutcome']
    X = df.drop('y',axis=1)
    Y = df['y']

    X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size =0.2,random_state=42)

    modellr = LogisticRegression(max_iter=5000)
    modeldt = RandomForestClassifier(n_estimators=100,random_state=42)
    modelknn = KNeighborsClassifier(n_neighbors=3)

    modellr.fit(X_train,Y_train)
    modeldt.fit(X_train,Y_train)
    modelknn.fit(X_train,Y_train)

    hard_model = VotingClassifier(
        estimators=[
            ('lr',modellr),
            ('dt',modeldt),
            ('knn',modelknn)
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

    
  

if __name__ == "__main__":
    main()