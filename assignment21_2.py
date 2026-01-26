import threading
def max(n):
    i=0
    print("Maximum number")
    if n > i:
        print(n)

def min(n):
    i=0
    print("Minimum number",)
    if n < i:
        print(i) 

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

    t1=threading.Thread(target=max,args=(Value,))
    t2=threading.Thread(target=min,args=(Value,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()
   
if __name__=="__main__":
    main()
