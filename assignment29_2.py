#Read the content from file
import os

def OpenFile(FileName):
    fobj=open(FileName,'r')
    print("Content of file:")
    print(fobj.read())

def main():
    FileName=input("Enter the name of file : ")
    OpenFile(FileName)
    
    
if __name__=="__main__":
    main()

