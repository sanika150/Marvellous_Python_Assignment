Max = lambda No1,No2:No1 if No1 > No2 else No2

def main():
    Ret=0
    print("Enter the first Number :")
    Value1= int(input())
    print("Enter the Second Number :")
    Value2= int(input())

    Ret=Max(Value1,Value2)
    print("Maximum number is: ",Ret)

    

if __name__ == "__main__":
    main()
    

