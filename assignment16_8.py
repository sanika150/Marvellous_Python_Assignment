def Display(No):
    i=0
    while (i<No):
        print("*",end=" ")
        i = i+1

    
def main():
   ret = 0
   print("Enter the number")
   Value=int(input())

   ret=Display(Value)
   #print(ret)
     
if __name__ == "__main__":
    main()
    

