def Chk(No):
    if No == 0:
        print("zero")
    elif No < 1:
        print("Negative")
    else:
        print("Positive")

    
def main():
   ret = 0
   print("Enter the number")
   Value=int(input())

   ret=Chk(Value)
     
if __name__ == "__main__":
    main()
    

