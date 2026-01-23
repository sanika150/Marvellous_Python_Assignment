Even = lambda No:No %2==0

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

    FData = list(filter(Even,Data))
    print("Filtered Data is: ",FData)
    
if __name__ == "__main__":
    main()
    

