#Check whether file is exists in current directory
import os

def CheckFile(FileName):
    if(os.path.exists(FileName)):  #check file exist or not
        print(f"{FileName} exist ")

    else:
        print("There is no such file")

def main():
    FileName=input("Enter the name of file : ")
    CheckFile(FileName)
    
    
if __name__=="__main__":
    main()

