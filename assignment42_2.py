import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error,r2_score

def main():
    X = [[1],[2],[3],[4],[5]]                 
    Y= [[3],[4],[2],[4],[5]]

    X_train, X_test , Y_train, Y_test = train_test_split(X,Y,test_size= 0.2)
    
    model = LinearRegression()

    model.fit(X_train, Y_train)

    Y_pred = model.predict(X_test)

    print("Testing data : ")
    print(X_test)

    print("Predicted values : ")
    print(Y_pred)

    print("Actual values : ")
    print(Y_test)

    MSE = mean_squared_error(Y_test,Y_pred)
    RMSE = np.sqrt(MSE)
    R2 = r2_score(Y_test,Y_pred)

    print("Mean Squared Error : ",MSE)
    print("Root Means Squared Error : ",RMSE)
    print("R Square Value : ",R2)

if __name__ == "__main__":
    main()