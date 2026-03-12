import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score,confusion_matrix,classification_report
import matplotlib as plt
from sklearn.preprocessing import StandardScaler

def MarvellousClassifier(DataPath):
    Border = "-"*40

    #Step 1:Load the dataset from CSV file
    print(Border)
    print("Step 1:Load the dataset from CSV file")
    print(Border)

    df=pd.read_csv(DataPath)
    print(Border)
    print("Some entries from dataset")
    print(df.head())
    print(Border)

    #step 2:clean the dataset by removing empty rows
    print(Border)
    print("step 2:clean the dataset by removing empty rows")
    print(Border)

    df.dropna(inplace=True)
    print("Total records : ",df.shape[0])
    print("TOtal columns : ",df.shape[1])
    print(Border)



    X = df.drop(columns = ['Class'])
    Y = df['Class']

    print("Shape of X : ",X.shape)
    print("Shape of Y : ",Y.shape)

   

    #step 4:Split the data set for training and testing
    

    X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,random_state=42,stratify=Y)

    print(Border)
    print("Information of training and testing data")
    print("X_train shape : ",X_train.shape)
    print("X_test shape : ",X_test.shape)
    print("Y_train shape : ",Y_train.shape)
    print("Y_test shape : ",Y_test.shape)
    print(Border)

    

    #step 6:Explore the multiple values of K 
    #Hyper parameter tunning(K)
    

    
    model = KNeighborsClassifier(n_neighbors=3)
    print(Border)
    print("step 3:Train the data")
    print(Border)
    model.fit(X_train,Y_train)

    print(Border)
    print("step 5:Test the data")
    print(Border)
    Y_Pred= model.predict(X_test)
    print(Border)
    print("step 4:Calculate accuracy")
    print(Border)
    accuracy = accuracy_score(Y_test,Y_Pred)
        
    print("Accuracy is : ",accuracy * 100)

def main():
    Border = "-"*40
    print(Border)
    print("Wine Classifier using KNN")
    print(Border)

    MarvellousClassifier("WinePredictor.csv")




if __name__ == "__main__":
    main()
