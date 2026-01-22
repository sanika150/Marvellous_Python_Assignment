def Odd(No):
    

    for i in range(1,No+1,2):
        print(i)
        

def main():
    
    print("Enter the no:")
    n=int(input())
    print(Odd(n)) 
   
if __name__ == "__main__":
    main()