def Frequency(Arr,n):
    frequency=0
    frequency=Arr.count(n)
    print("output: ",frequency)
        

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

    value= int(input("Element to search"))

    Ret= Frequency(data,value)
   
if __name__ == "__main__":
    main()

