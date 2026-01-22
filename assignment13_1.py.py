def Area(a,b):
    area=1
    area=a*b
    return area
        
def main():
    Ans=0
    print("Enter the length of Rectangle:")
    l=int(input())

    print("Enter the width of Rectangle:")
    w=int(input())
    Ans=Area(l,w)
    print("Area of Rectangle is:",Ans)
   
if __name__ == "__main__":
    main()