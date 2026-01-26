import threading

def Small(s):
    count=sum(1 for ch in s if ch.islower())
    t=threading.current_thread()
    print("Lowercase count: ",count)
    print("Thread Id: ",t.ident)
    print("Thread Name: ",t.name)
    print()
    
def Capital(s):
    count=sum(1 for ch in s if ch.isupper())
    t=threading.current_thread()
    print("Uppercase count: ",count)
    print("Thread Id: ",t.ident)
    print("Thread Name: ",t.name)
    print()

def Digit(s):
    count=sum(1 for ch in s if ch.isdigit())
    t=threading.current_thread()
    print("Digit count: ",count)
    print("Thread Id: ",t.ident)
    print("Thread Name: ",t.name)
    print()
    

def main():
    string=input("Enter a string: ")
    t1=threading.Thread(target=Small,args=(string,))
    t2=threading.Thread(target=Capital,args=(string,))
    t3=threading.Thread(target=Digit,args=(string,))

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

    
    
   
if __name__=="__main__":
    main()
