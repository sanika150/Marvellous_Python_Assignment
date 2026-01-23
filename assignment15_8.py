#from functools import reduce

Divisible = lambda a:a % 3 == 0 and a % 5==0 

       
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

    FData = list(filter(Divisible,Data))
    print("Number divisible by 3 and 5: ",FData)
    
if __name__ == "__main__":
    main()
    

