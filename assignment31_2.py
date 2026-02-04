#change the extension of file
import sys
import os

def DirectoryScanner(DirName,old_ext,new_ext):
    
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
            if fname.endswith(old_ext):
                path = os.path.join(DirName,fname)
                new_file=fname.replace(old_ext,new_ext)
                new_path=os.path.join(DirName,new_file)
                os.rename(path,new_path)
                print(f"renamed file :{fname}-> {fname}{new_file}")

def main():
  

    DirectoryScanner(sys.argv[1],sys.argv[2],sys.argv[3])

if __name__=="__main__":
    main()