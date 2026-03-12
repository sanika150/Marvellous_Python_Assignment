import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score,confusion_matrix,classification_report
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder


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

    print("step 2 : Remove unwanted column")
    print(Border)

    print("Shape of dataset before removal : ",df.shape)
    if 'Unnamed: 0' in df.columns:
        df.drop(columns=['Unnamed: 0'],inplace=True)
        print("Shape of dataset after removal : ",df.shape)
    #step 2:clean the dataset by removing empty rows
    print(Border)
    print("step 2:clean the dataset by removing empty rows")
    print(Border)

    df.dropna(inplace=True)
    print("Total records : ",df.shape[0])
    print("Total columns : ",df.shape[1])
    print(Border)

    #step 3:Separate independent and dependent variables
    print(Border)
    print("step 3:Separate independent and dependent variables")
    print(Border)

    Whether = df['Whether']
    Temperature = df['Temperature']
    Play = df['Play']

    weather_encoder = LabelEncoder()
    temp_encoder = LabelEncoder()
    play_encoder = LabelEncoder()

    df['encoded_Whether'] = weather_encoder.fit_transform(Whether)
    df['encoded_Temperature'] = temp_encoder.fit_transform(Temperature)
    df['encoded_Play'] = play_encoder.fit_transform(Play)

    X = df[['encoded_Whether','encoded_Temperature']]
    Y = df['encoded_Play']

  


    #step 4:Split the data set for training and testing
    print(Border)
    print("step 4:Split the data set for training and testing")
    print(Border)

    X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,random_state=42)

    print(Border)
    print("Information of training and testing data")
    print("X_train shape : ",X_train.shape)
    print("X_test shape : ",X_test.shape)
    print("Y_train shape : ",Y_train.shape)
    print("Y_test shape : ",Y_test.shape)
    print(Border)

    
    model = KNeighborsClassifier(n_neighbors=3)
    #instance method
    model.fit(X_train,Y_train)

    Y_pred = model.predict(X_test)
   

    accuracy = accuracy_score(Y_test,Y_pred)

    print("Accuracy is : ",accuracy * 100)

    print(Border)

    
def main():
    Border = "-"*40
    print(Border)
    print("Wine Classifier using KNN")
    print(Border)

    MarvellousClassifier("PlayPredictor.csv")




if __name__ == "__main__":
    main()
