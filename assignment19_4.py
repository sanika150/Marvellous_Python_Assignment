from functools import reduce


Even =lambda No: No%2==0

Square=lambda No:No*No
Add = lambda A,B:A+B
        

def main():
    Ret = 0
    size = 0
    Value =0

    print("Enter the number of elements:")
    size = int(input())

    Data = list()

    print("Enter the elements :")
    for i in range(size):
        Value = int(input())
        Data.append(Value)

    print("Given data:",Data)

    FData= list(filter(Even,Data))
    print("Filtered data is:",FData)

    MData = list(map(Square,FData))
    print("Mapped data is:",MData)

    RData = reduce(Add,MData)
    print("Reduced data is:",RData)


if __name__ == "__main__":
    main()

