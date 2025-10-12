# Calculator 
def add(P, Q):
    return P + Q

def subtract(P, Q):
    return P - Q

def multiply(P, Q):
    return P * Q

def divide(P, Q):
    return P / Q

while True:
    print("Please select the operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = input("Enter your choice (1/2/3/4): ")

    num1 = float(input("Please enter first number: "))
    num2 = float(input("Please enter second number: "))

    if choice == "1":
        print(num1, "+", num2, "=", add(num1, num2))
    elif choice == "2":
        print(num1, "-", num2, "=", subtract(num1, num2))
    elif choice == "3":
        print(num1, "*", num2, "=", multiply(num1, num2))
    elif choice == "4":
        if num2 == 0:
            print("Error: Cannot divide by zero!")
        else:
            print(num1, "/", num2, "=", divide(num1, num2))
    else:
        print("Invalid Input!")

    again = input("Do you want to calculate again? (y/n): ").lower()
    if again != 'y':
        print("Thank you for using the calculator! 😊")
        break
