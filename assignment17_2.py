def Display(n):
    i =0
    j=0
   
    for i in range(n):
        
        for j in range(n):
            print("*",end=" ")
            
        print()

def main():
    #Result = 0
    print("Enter the first number")
    No=int(input())
    Display(No)

if __name__ == "__main__":
    main()

