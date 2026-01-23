Even = lambda No:True if No % 2==0 else False

def main():
    Ret=0
    print("Enter the first Number :")
    Value= int(input())
    

    Ret=Even(Value)
    print(Ret)

    

if __name__ == "__main__":
    main()
    

