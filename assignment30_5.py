#searcch word in file
import os

def CheckWord(FileName,word):

    fobj=open(FileName,"r")
    for line in fobj:
        if word in line:
            return True
        else:
            return False
def main():
    Ret = 0
    FileName=input("Enter the name of file : ")
    Word=input("Enter the word you want to search : ")
    Ret =CheckWord(FileName,Word)
    if Ret == True:
        print(f"{Word} present in {FileName}")
    else:
        print("Word is not present")
    
    
if __name__=="__main__":
    main()
