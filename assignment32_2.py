import hashlib
import os
import sys

def CalculateCheckSum(FileName):
    fobj=open(FileName,"rb") #binary mode

    hobj = hashlib.md5()
    #it  read chunk by chunk
    buffer = fobj.read(1000) # it will read first 1kb data
    while (len(buffer)>0): #check upto size greater than 0 kb
        hobj.update(buffer)
        buffer = fobj.read(1000)
        

    fobj.close()

    return hobj.hexdigest()

def FindDuplicate(DirectoryName ):
    Border = "-"*50
    Ret = False
    Ret = os.path.exists(DirectoryName)
    if (Ret == False):
        print("There is no such directory")
        return
    
    Ret = os.path.isdir(DirectoryName)
    if (Ret == False):
        print("IT is not directory")
        return
    
    Duplicate = {} #dictionary
    log=open("Log.txt","w")  #write mode thn create if not present
    
    log.write(Border+"\n")
    log.write("This is a log file created by marvellous automation\n")
    log.write("Duplicate files in directory\n")
    for FolderNme,SubFolderName,FileName in os.walk(DirectoryName):
        for fname in FileName:
            fname = os.path.join(FolderNme,fname)
            CheckSum = CalculateCheckSum(fname)

            if CheckSum in Duplicate:
                log.write(fname+"\n")
            else:
                Duplicate[CheckSum] = [fname]
        return Duplicate #return duplicate dictionary
    log.write(Border+"\n")
    log.close()




def main():
   Ret = FindDuplicate(sys.argv[1])
   
if __name__ =="__main__":
    main()