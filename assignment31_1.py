#Display file with user define extension
import sys
import os

def DirectoryScanner(DirName,Ext):
    
    Ret = os.path.exists(DirName)
    if Ret == False:
        print("There is no such directory")
        return
    
    Ret = os.path.isdir(DirName)
    if Ret == False:
        print("It is not a directory")
        return
    
    print("Files with given extensions are: ")
    for FolderName,SubFolder,FileName in os.walk(DirName):
        for fname in FileName:
            if fname.endswith(Ext):
                print(fname)

def main():
  

    DirectoryScanner(sys.argv[1],sys.argv[2])

if __name__=="__main__":
    main()