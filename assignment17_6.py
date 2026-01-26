def Display(n):
    i =0
    j=0
   
    for i in range(n,0,-1):
        
        for j in range(1,i+1):
            print("*",end=" ")
            
        print()

def main():
    #Result = 0
    print("Enter the first number")
    No=int(input())
    Display(No)

if __name__ == "__main__":
    main()

