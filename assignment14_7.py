Divisible = lambda No:True if No % 5 == 0 else False

def main():
    Ret=0
    print("Enter the first Number :")
    Value= int(input())
    

    Ret=Divisible(Value)
    print(Ret)

    

if __name__ == "__main__":
    main()
    

