from functools import reduce

Add = lambda No1,No2:No1+No2

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

    RData = reduce(Add,Data)
    print("Addition of all elements: ",RData)
    
if __name__ == "__main__":
    main()
    

