import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error,r2_score
import matplotlib.pyplot as plt

def main():
    Study_Hours= [[1],[2],[3],[4],[5]]                 
    Marks= [[50],[55],[60],[65],[70]]

    X_train, X_test , Y_train, Y_test = train_test_split(Study_Hours,Marks,test_size= 0.2)
    
    model = LinearRegression()

    model.fit(X_train,Y_train)

    predicted_Marks=model.predict(X_test)

    print("Predicted Marks for 6 hours of study is : ",predicted_Marks)

    mse = mean_squared_error(Y_test, predicted_Marks)
    r2 = r2_score(Y_test, predicted_Marks)

    print("Mean Squared Error: ", mse)
    print("R-squared: ", r2)
    print("step 11 : Calculate model coefficient")
    

    for column,value in zip(Study_Hours,model.coef_):
        print(f"{column}:{value}")

    print("Intercept : ",model.intercept_)


   

  

if __name__ == "__main__":
    main()