#Compare two files
import os
import sys

def CompareFile():
    
    fobj=open(sys.argv[1],"r")
    fobj1=open(sys.argv[2],"r")

    if fobj.read() == fobj1.read():
        print("Success")
    else:
        print("Failure")

def main():
    
    CompareFile()
    
    
if __name__=="__main__":
    main()

