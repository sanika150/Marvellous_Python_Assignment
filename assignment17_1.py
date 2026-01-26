import Arithmetic

Result = 0
print("Enter the first number")
No1=int(input())

print("Enter the second number")
No2=int(input())
Result = Arithmetic.Add(No1,No2)
print("Addition is : ",Result)

Result = Arithmetic.Sub(No1,No2)
print("Subtraction is : ",Result)

Result = Arithmetic.Mul(No1,No2)
print("Subtraction is : ",Result)

Result = Arithmetic.Div(No1,No2)
print("Subtraction is : ",Result)