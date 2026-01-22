def main():
    
    print("Enter the no:")
    No1=int(input())
    if No1 % 3 == 0 and No1 % 5 ==0:
        print("Divisible by 3 and 5")
    else:
        print("Not divisible by 3 and 5")
    
if __name__ == "__main__":
    main()