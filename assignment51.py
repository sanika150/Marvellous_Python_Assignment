from turtle import distance

import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import VotingClassifier
from sklearn.metrics import accuracy_score,confusion_matrix,classification_report,ConfusionMatrixDisplay
import matplotlib.pyplot as plt
import seaborn as sns

from BaggingClassificationBreastCancer import Y_train


# Load your data into a DataFrame (example with a hypothetical 'df' and 'target_variable')
# df = pd.read_csv('your_data.csv')


def main():
    Border = "-" *50
    print(Border)
    fake_df =pd.read_csv("Fake.csv")
    true_df =pd.read_csv("True.csv")
     #Add labrls
    fake_df["label"]=0
    true_df["label"]=1

    df = pd.concat([fake_df,true_df],axis=0)

    df=df.sample(frac=1,random_state=42).reset_index(drop=True)

    print(df.head())
   
    df["content"]=df["title"]+" "+df["text"]

    df.dropna(inplace=True)

   

    X=df["content"]
    Y=df["label"]

    X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size =0.2,random_state=42)

    modellr = LogisticRegression(max_iter=5000)
    modeldt = DecisionTreeClassifier()
    
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

    soft_model = VotingClassifier(
        estimators=[
            ('lr',modellr),
            ('dt',modeldt)
        ],
        voting='soft'
    )

    soft_model.fit(X_train,Y_train)


    #evaluation
    y_pred_lr = modellr.predict(X_test)
    y_pred_dt = modeldt.predict(X_test)
    
    pred_hard = hard_model.predict(X_test)
    pred_soft = soft_model.predict(X_test)

    
    acc_hard = accuracy_score(pred_hard,Y_test)
    print(Border)
    print("Hard voting accuracy : ",acc_hard)
    print(Border)

    acc_lr = accuracy_score(y_pred_lr,Y_test)
    print(Border)
    print("lraccuracy : ",acc_lr)
    print(Border)

    acc_dt = accuracy_score(y_pred_dt,Y_test)

    print(Border)
    print("dtaccuracy : ",acc_dt)
    print(Border)

    acc_soft = accuracy_score(pred_soft,Y_test)
    print(Border)
    print("Soft voting accuracy : ",acc_soft)
    print(Border)

   

    
  

if __name__ == "__main__":
    main()