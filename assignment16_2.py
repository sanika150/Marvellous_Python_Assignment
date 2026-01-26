def Even(Value):
    if Value % 2 == 0:
        return True
    else:
        return False
    

       
def main():
   Ret=0
   print("Enter the number ")
   No=int(int(input()))

   Ret=Even(No)
   if Ret == True:
       print("Even number")
   else:
       print("Odd number")
      
   
    
if __name__ == "__main__":
    main()
    

