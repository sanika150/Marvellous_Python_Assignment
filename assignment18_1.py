def Addition(Arr):
    sum = 0
    for i in range(len(Arr)):
        sum=sum + Arr[i]
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

    Ret= Addition(data)
    print("Summation is: ",Ret)
if __name__ == "__main__":
    main()

