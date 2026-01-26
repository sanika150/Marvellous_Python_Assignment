def Display(n):
    sum = 0
    last=0

    while n != 0:
        last = n % 10
        sum = sum+last
        n //= 10
    return sum




def main():
    Result = 0
    print("Enter the  number")
    No=int(input())
    Result=Display(No)
    print("Result is:",Result)
   
if __name__ == "__main__":
    main()

