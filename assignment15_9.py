from functools import reduce

Product = lambda a,b:a*b 

       
def main():
    size=0
    value=0
    print("Enter the size of element")
    size = int(input())
    Data = list()
    print("Enter the Element:")
    for i in range(size):
        value = int(input())
        Data.append(value)

    print("Data is: ",Data)

    RData = reduce(Product,Data)
    print("Product of all numbers: ",RData)
    
if __name__ == "__main__":
    main()
    

