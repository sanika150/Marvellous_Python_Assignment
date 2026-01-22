def Prime(N):
    i = 1
    if(N<=1):
        print("Not Prime number")
    else:
        for i in range(2,int(N**0.5)+1):
            if N % i == 0:
                print("Not prime number")
                break
        else:
            print("Prime number")
       
def main():
    print("Enter the first Number :")
    No= int(input())
    Prime(No)

if __name__ == "__main__":
    main()
    