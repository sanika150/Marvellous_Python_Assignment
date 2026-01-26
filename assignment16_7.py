def Divisible(No):
    if No % 5 == 0:
        return True
    else:
        return False

    
def main():
   ret = 0
   print("Enter the number")
   Value=int(input())

   ret=Divisible(Value)
   print(ret)
     
if __name__ == "__main__":
    main()
    

