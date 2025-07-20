Proj1:"Basic Calculator App"
#step1:Define calculator Function(Basic Arithematic Function)
def add(x,y):
    return x+y
def substract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    if y==0:
        return "error! division by zero is not allowed"
    else:
        return x/y 

#step2:Create a user interface
def calculator():
    print("Simple calculator")
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")

choice=input("Enter Your choice(1/2/3/4):")    

if choice in['1','2','3','4']:
    num1=float(input("Enter First Number:"))
    num2=float(input("Enter Second Number:"))

if choice == '1':
    print(f"{num1}+{num2} = {add(num1,num2)}")   
elif choice == '2':
    print(f"{num1}-{num2} = {substract(num1,num2)}")
elif choice == '3':
    print(f"{num1}*{num2} = {multiply(num1,num2)}")
elif choice == '4':
    print(f"{num1}/{num2} = {divide(num1,num2)}")
else:
    print("Invalid choice")

#Run the Calculator
calculator()        
