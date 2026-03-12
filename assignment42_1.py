import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def MarvellousPredictor():
    # Load the data
    X = [1,2,3,4,5]
    Y = [3,4,2,4,5]

    print("Values of Independent variables : X - ",X)
    print("Values of Dependent variables : Y - ",Y)

    mean_x = np.mean(X)
    mean_y = np.mean(Y)

    print("mean of X : ",mean_x)    

    print("mean of Y : ",mean_y)    

    n = len(X)  


    numerator = 0
    denominator = 0

    for i in range(n):
        numerator = numerator + ((X[i] - mean_x) * (Y[i] - mean_y))
        denominator = denominator + ((X[i] - mean_x)**2)

    m = numerator / denominator

    print("Slope m = ",m)    

    C = mean_y - (m * mean_x)

    print("intercept C  = ",C)

    print("Eqaution of line is : Y=",m,"X +",C)
    
def main():
    MarvellousPredictor()

if __name__ == "__main__":
    main()