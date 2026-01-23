Square = lambda No:No * No

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

    MData = list(map(Square,Data))
    print("MData is: ",MData)
    
if __name__ == "__main__":
    main()
    

