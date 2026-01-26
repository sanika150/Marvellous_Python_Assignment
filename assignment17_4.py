def Factorial(n):
    i =0
    sum=0
   
    for i in range(1,n+1):
        if n % i == 0:
            sum += i
        
    print("Sum of factors:",sum)

def main():
    #Result = 0
    print("Enter the first number")
    No=int(input())
    Factorial(No)

if __name__ == "__main__":
    main()

