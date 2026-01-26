import threading
lobj = threading.Lock()
def Display():
    for i in range(1,51):
        with lobj:
         print(i,end=" ")
         
    
def Reverse_Display():
    print("\n Reverse number")
    for i in range(50,0,-1):
        print(i,end=" ")
  
    

def main():
    
    t1=threading.Thread(target=Display())
    t2=threading.Thread(target=Reverse_Display())
    
    t1.start()
    t2.start()
    
    t1.join()
    t2.join()
    
    

    
    
   
if __name__=="__main__":
    main()
