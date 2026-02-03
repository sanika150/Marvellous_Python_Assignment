#copy the content from one file to other
import os
import sys

def CopyFile():
    File="Demo.txt"
    fobj=open(sys.argv[1],"r")
    data = fobj.read()

    fobj2=open(File,"w")
    fobj2.write(data)
    print(f"file data copied into Demo.txt")

def main():
    
    CopyFile()
    
    
if __name__=="__main__":
    main()

