#Count words in file
import os
import sys

def CountWord(FileName):
    count = 0

    fobj=open(FileName,"r")
    for line in fobj:
        words = line.split()
        count=count + len(words)
    print("Total number of words: ",count)
    
    
def main():
    
    FileName=input("Enter the filename : ")
    
    
    CountWord(FileName)

    
if __name__=="__main__":
    main()

