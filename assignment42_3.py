import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error,r2_score
import matplotlib.pyplot as plt

def main():
    experience = [[1],[2],[3],[4],[5]]                 
    salary= [[20000],[25000],[30000],[35000],[40000]]

    #X_train, X_test , Y_train, Y_test = train_test_split(experience,salary,test_size= 0.2)
    
    model = LinearRegression()

    model.fit(experience,salary)

    predicted_salary=model.predict([[6]])

    print("Predicted salary for 6 years of experience is : ",predicted_salary)

    plt.scatter(experience,salary,label="Data Points")

    plt.plot(experience,model.predict(experience),label ="Regression Line")

    plt.show()
   

  

if __name__ == "__main__":
    main()