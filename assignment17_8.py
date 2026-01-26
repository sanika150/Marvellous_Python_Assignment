def Display(n):
    i =0
    j=0
    No=1
    for i in range(0,n):
        No=1
        for j in range(0,i+1):
            print(No,end=" ")
            No=No+1
        print()

def main():
    #Result = 0
    print("Enter the first number")
    No=int(input())
    Display(No)

if __name__ == "__main__":
    main()

