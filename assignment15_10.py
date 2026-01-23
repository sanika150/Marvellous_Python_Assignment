from functools import reduce

Even = lambda a: a% 2 ==0

       
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

    FData = len(list(filter(Even,Data)))
    print("Count of even numbers: ",FData)
    
if __name__ == "__main__":
    main()
    

