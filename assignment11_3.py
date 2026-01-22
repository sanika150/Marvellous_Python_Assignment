def Sum(N):
    digit =0
    for i in N:
        digit += int(i)
    print("Sum of digit: ",digit)
       
def main():
    print("Enter the first Number :")
    No= (input())
    Sum(No)

if __name__ == "__main__":
    main()
    

