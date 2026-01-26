import threading

def EvenFactor(Arr):
    Even=[]
    i=0
    for i in range(1,Arr+1):
        if Arr % i == 0 and i % 2==0:
            Even.append(i)
    print("Even Factors: ",Even)
    print("Sum of even factors: ",sum(Even))
    

def OddFactor(Arr):
    Odd=[]
    for i in range(1,Arr+1):
        if Arr % i == 0 and i % 2!=0:
            Odd.append(i)
    print("Even Factors: ",Odd)
    print("Sum of even factors: ",sum(Odd))
    

def main():
    size = 0
    Value =0

    print("Enter the number of elements:")
    size = int(input())

    Data = list() 

    print("Enter the elements :")
    for i in range(size):
        Value = int(input())
        Data.append(Value)

    t1=threading.Thread(target=EvenFactor,args=(Value,))
    t2=threading.Thread(target=OddFactor,args=(Value,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Exit from main")
    
   
if __name__=="__main__":
    main()
