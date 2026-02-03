#Display  content line by line

def Display(FileName):
   

    fobj=open(FileName,"r")
    for line in fobj:
        print(line+"\n")
    
    
def main():
    
    FileName=input("Enter the filename : ")
    
    
    Display(FileName)

    
if __name__=="__main__":
    main()

