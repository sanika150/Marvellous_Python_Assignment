Largest = lambda No1,No2,No3:(No1 if(No1 > No2 and No1> No3)else No2 if No2 > No3 else No3)

def main():
    Ret=0
    print("Enter the first Number :")
    Value1= int(input())
    print("Enter the second Number :")
    Value2= int(input())
    print("Enter the third Number :")
    Value3= int(input())
    

    Ret=Largest(Value1,Value2,Value3)
    print("Largest number is:",Ret)

    
if __name__ == "__main__":
    main()
    

