import threading
sum_result = 0
product_result=0
def Sum(n):
    global sum_result 
    for i in range(n):
        sum_result = n + i
    

def Product(n):
   global product_result
   for i in range(n):
      product_result = n * i 
    

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

    t1=threading.Thread(target=Sum,args=(Value,))
    t2=threading.Thread(target=Product,args=(Value,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    
    print("Sum of element",sum_result)
    print("Product of element",product_result)
   
if __name__=="__main__":
    main()
