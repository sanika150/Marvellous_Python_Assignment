import pandas as pd
import numpy as np

def main():
  #  X= [[Study_Hours],[Sleep_Hours]]
    X = [[6],[7],[8],[9],[10],[11],[12]]   
                 

    mean_x = np.mean(X)
    
    Std= np.std(X)
    

    print("Mean of dataset is : ",mean_x)
    print("Standard Deviation of dataset is : ",Std)
 


   

  

if __name__ == "__main__":
    main()