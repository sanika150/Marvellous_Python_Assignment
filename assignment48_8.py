from turtle import distance

import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.metrics.pairwise import euclidean_distances
from sklearn.metrics import accuracy_score,confusion_matrix

def main():
  #  X= [[Study_Hours],[Sleep_Hours]]
    actual = [[1],[1],[1],[1],[0],[0],[0],[0]]
    predicted = [[1],[1],[0],[1],[0],[1],[0],[0]]   
                 
    cm = confusion_matrix(actual,predicted)

    print("Confusion matrix is : ")
    print(cm)


  

if __name__ == "__main__":
    main()