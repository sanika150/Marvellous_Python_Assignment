from turtle import distance

import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.metrics.pairwise import euclidean_distances

def main():
  #  X= [[Study_Hours],[Sleep_Hours]]
    X = [[25],[30],[35]]
    Y = [[20000],[40000],[60000]]   
                 
    distance = euclidean_distances(X,Y)
    print("Distance is: \n",distance)

    scalar = StandardScaler()
    X_scaled = scalar.fit_transform(X)
    Y_scaled = scalar.fit_transform(Y)

    Scaled_distance = euclidean_distances(X_scaled, Y_scaled)
    print("Scaled_distance is : \n",Scaled_distance)

  

if __name__ == "__main__":
    main()