import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error,r2_score


def main():
    Study_Hours= [[1],[2],[3],[4],[5]]                 
    Marks= [[50],[55],[60],[65],[70]]

 
    
    model = LinearRegression()

    model.fit(Study_Hours,Marks)

    predicted_Marks=model.predict([[6]])

    print("Predicted Marks for 6 hours of study is : ",predicted_Marks)

   
   
   

  

if __name__ == "__main__":
    main()