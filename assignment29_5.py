##Frequency of String
import os
import sys

def Frequency(FileName,String):
    count = 0
    fobj=open(FileName,"r")
    for line in fobj:
        count=count + line.count(String)
    
    print(f"Frequency of {String} in {FileName} is : ",count)
    
def main():
    FileName=input("Enter the filename : ")
    String=input("Enter the string to search : ")
    
    Frequency(FileName,String)
    
    
if __name__=="__main__":
    main()

