def Factorial(n):
    i =0
    fact=1
   
    for i in range(1,n+1):
        fact *= i
            
    print("Factorial:",fact)

def main():
    #Result = 0
    print("Enter the first number")
    No=int(input())
    Factorial(No)

if __name__ == "__main__":
    main()

