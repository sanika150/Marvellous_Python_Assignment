#copy files to other dir
import sys
import os
import shutil

def DirectoryCopy(DirName,New_dir):
    Ret = os.path.isdir(DirName)
    if Ret == False:
        print("It is not a directory")
        return
    
    if not os.path.exists(New_dir):
        os.mkdir(New_dir)
        
    for FileName in os.listdir(DirName):
        src_path=os.path.join(DirName,FileName)
        des_path=os.path.join(New_dir,FileName)

        if os.path.isfile(src_path):
            shutil.copy(src_path,des_path)
            print(f"Copied: {FileName}")

def main():
    if len(sys.argv)!=3:
        return
    DirectoryCopy(sys.argv[1],sys.argv[2])

if __name__=="__main__":
    main()