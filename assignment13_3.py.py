def Perfect(n):
    a=0
    i=0
    for i in range(1,n):
        if(n % i==0):
             a=a+i
    if (a==n):
        print("Perfect number")
    else:
        print("Not a perfect number")
        
def main():
    
    print("Enter the Number:")
    No=int(input())
    Perfect(No)
   
if __name__ == "__main__":
    main()