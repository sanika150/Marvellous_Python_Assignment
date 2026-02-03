#Count the total number of lines from file
import os
import sys

def Count(FileName):
    count = 0

    fobj=open(FileName,"r")
    for line in fobj:
        count=count + 1
    return count
    
def main():
    Ret = 0
    FileName=input("Enter the filename : ")
    
    
    Ret = print("Total no of lines are : " ,Count(FileName))

    
if __name__=="__main__":
    main()

