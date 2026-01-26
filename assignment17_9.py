def Display(n):
    count = 0

    while n >0:
        count = count+1
        n //= 10
    print("Number of digits: ",count)


def main():
    #Result = 0
    print("Enter the  number")
    No=int(input())
    Display(No)

if __name__ == "__main__":
    main()

