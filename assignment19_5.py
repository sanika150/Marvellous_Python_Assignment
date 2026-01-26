from functools import reduce


def ChkPrime(n):
    i = 0
    if n < 2:
        return False
    
    for i in range (2,int(n/2)+1):
        if n % i == 0:
            return False
    return True

Mul=lambda No:No*No
Max = lambda A,B:A if A>B else B
        

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

    FData= list(filter(ChkPrime,Data))
    print("Filtered data is:",FData)

    MData = list(map(Mul,FData))
    print("Mapped data is:",MData)

    RData = reduce(Max,MData)
    print("Reduced data is:",RData)


if __name__ == "__main__":
    main()

