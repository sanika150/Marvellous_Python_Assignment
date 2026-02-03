#copy the content from existing file to new file
import os
import sys

def CopyFile(FileName,NewFile):
   # File="Demo.txt"
    fobj=open(FileName,"r")
    data = fobj.read()

    fobj2=open(NewFile,"w")
    fobj2.write(data)
    print(f"{FileName}  data copied into {NewFile}")

def main():
    FileName=input("Enter the filename : ")
    NewFile=input("Enter the New filename : ")
    CopyFile(FileName,NewFile)
    
    
if __name__=="__main__":
    main()

