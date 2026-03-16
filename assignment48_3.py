import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
def main():
  #  X= [[Study_Hours],[Sleep_Hours]]
    X = [[25],[30],[35]]
    Y = [[20000],[40000],[60000]]   
                 

    scalar = StandardScaler()
    X_scaled = scalar.fit_transform(X)
    Y_scaled = scalar.fit_transform(Y)

    print("Data after scalling : ")
    print("X_scaled: \n", X_scaled)
    print("Y_scaled: \n", Y_scaled)


  

if __name__ == "__main__":
    main()