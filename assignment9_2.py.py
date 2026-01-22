print("Enter first no:")
No1=int(input())
print("Enter second no:")
No2=int(input())

def ChkGreater():
    if No1 > No2:
        print(No1,"is greater")
    else:
        print(No2,"is greater")

def main():


    ChkGreater()


if __name__ == "__main__":
    main()