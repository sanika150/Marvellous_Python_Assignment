def Sum(n):
    i=1
    sum=0
    
    while i <= n:
        sum = sum + i
        i = i+1
    return sum
def main():
    
    print("Enter the no:")
    n=int(input())
    print(Sum(n)) 
   
if __name__ == "__main__":
    main()