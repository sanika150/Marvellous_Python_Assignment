def Area(a):
    area=0
    area=a*a
    return area
        
def main():
    Ans=0
    print("Enter the Radius of Circle:")
    r=int(input())

    Ans=Area(r)
    print("Area of Rectangle is:",Ans)
   
if __name__ == "__main__":
    main()