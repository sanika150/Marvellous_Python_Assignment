def factor(No):
    i=0
    for i in range(1,No+1):
        if No % i ==0:
            print(i) 
        
def main():
    Res =0
    print("Enter the Number :")
    No= int(input())
    Res=factor(No)
    

if __name__ == "__main__":
    main()
    