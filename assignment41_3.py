
import numpy as np
import math

def EucDistance(P1,P2):
    Ans = math.sqrt((P1['X']-P2['X'])**2 + (P1['Y']-P2['Y'])**2)

    return Ans

def MarvellousKNeighbourClassifier():
    Border = "-"*40
    data = [[2,60,"Fail"],
            [5,80,"Pass"],
            [6,85,"Pass"],
            [1,50,"Fail"],
            ]
    
    

    print(Border)

    study_hours=int(input("Enter Study Hours: "))
    
    attendance=int(input("Enter Attendance: "))
    #new_point=[Study_hours,attendance]
   

    distances =[]
       
    for row in data:
        dist=math.sqrt((study_hours - row[0])**2 + (attendance - row[1])**2)
        distances.append((dist,row[2]))

    distances.sort()
   

    print(Border)

    K=3
    neighbors = distances[:K]

    pass_count = 0
    fail_count = 0

    for n in neighbors:
        if n[1] == "Pass":
            pass_count += 1
        else:
            fail_count += 1

    if pass_count >fail_count:
        result = "Pass"
    else:
        result = "Fail"

    print("Predicted Result : ",result)

def main():
    MarvellousKNeighbourClassifier()

if __name__ == "__main__":
    main()

