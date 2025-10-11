def add(P,Q):
    return P + Q
def subtract(P,Q):
    return P - Q
def multiply(P,Q):
    return P * Q
def divide(P,Q):
    return P / Q

print("please Select the operation: ")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

choice = input("Enter your choice(1/2/3/4):")

num1 = int(input("Please Enter first number: "))
num2 = int(input("Please Enter second number: "))

if choice == "1":
    print(num1,"+",num2,"=",add(num1,num2))
    
elif choice == "2":
    print(num1,"-",num2,"=",subtract(num1,num2))
elif choice == "3":
    print(num1,"*",num2,"=",multiply(num1,num2))
elif choice == "4":
    print(num1,"/",num2,"=",divide(num1,num2))
else:
    print("This is an Invalid Input")

