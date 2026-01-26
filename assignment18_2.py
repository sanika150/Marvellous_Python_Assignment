def Maximum(Arr):
    res = Arr[0]
    for i in Arr:
        if i > res:
            res=i
    print("Maximum no is: ",res)
  

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

    Ret= Maximum(data)
   
if __name__ == "__main__":
    main()

