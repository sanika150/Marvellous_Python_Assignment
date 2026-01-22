def palindrom(N):
    if N == N[::-1]:
        print("Palindrome")
    else:
        print("Not a Palindrome")
def main():
    print("Enter the first Number :")
    No= (input())
    palindrom(No)
if __name__ == "__main__":
    main()
    

