

Power=lambda No:2 **No
        

def main():
    Ret = 0
    print("Enter first number :")
    No= int(input())
    Ret = Power(No)
    print("Power of number is: ",Ret)

if __name__ == "__main__":
    main()

