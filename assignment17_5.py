def Factorial(n):
    i =0
    sum=0

    if n <= 1:
        print("Not a prime number")
    else:
        for i in range(2,n):
            if n % i  == 0:
                print("Not a prime number")
                break
        else:
            print("It is prime number")
   


def main():
    #Result = 0
    print("Enter the  number")
    No=int(input())
    Factorial(No)

if __name__ == "__main__":
    main()

