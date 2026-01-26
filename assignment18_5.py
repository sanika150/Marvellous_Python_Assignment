import MarvellousNum

def ListPrime(Arr):
   sum = 0
   i = 0
   for i in Arr:
       if MarvellousNum.ChkPrime(i):
           sum = sum + i
           return sum
        

def main():
    Ret = 0
    size = 0
    print("Enter the  number of element")
    size=int(input())
    data=list()
    print("Enter the element")
    for i in range(size):
        value = int(input())
        data.append(value)

    Ret= ListPrime(data)
    print("Additio on prime numbers: ",Ret)
   
if __name__ == "__main__":
    main()

