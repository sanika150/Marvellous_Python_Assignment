def Even(No):
    for i in range(2,No+1,2):
        print(i)
        

def main():
    
    print("Enter the no:")
    n=int(input())
    print(Even(n)) 
   
if __name__ == "__main__":
    main()