def Add(No1,No2):
    sum = 0
    sum = No1+No2
    return sum

    
def main():
   Ret=0
   print("Enter the first number ")
   Value1=int(int(input()))

   print("Enter the second number ")
   Value2=int(int(input()))

   Ret=Add(Value1,Value2)
   print("Sum of two numbers is: ",Ret)
      
   
    
if __name__ == "__main__":
    main()
    

