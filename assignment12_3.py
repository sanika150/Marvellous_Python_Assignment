def Addition(value1, value2):
    Ans1 = 0   
    Ans1 = value1 + value2
    return Ans1

def Subtraction(value1, value2):
    Ans2 = 0   
    Ans2 = value1 - value2
    return Ans2

def Multiplication(value1, value2):
    Ans3 = 0   
    Ans3 = value1 * value2
    return Ans3

def Division(value1, value2):
    Ans4 = 0  
    Ans4 = value1 / value2
    return Ans4

def main():
    Res1 =0
    Res2 =0
    Res3 =0
    Res4 =0

    print("Enter the first Number :")
    No1= int(input())

    print("Enter the second Number :")
    No2= int(input())
   
    Res1 = print("Addition is: ",Addition(No1,No2))
    Res2 = print("Subtraction is: ",Subtraction(No1,No2))
    Res3 = print("Multiplication is: ",Multiplication(No1,No2))
    Res4 = print("Division is: ",Division(No1,No2))
    

if __name__ == "__main__":
    main()
    