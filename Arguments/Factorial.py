def factorial(x):
    '''this is a recursive function to find the factorial of an Integer '''

    if x==1 or x==0:
        return 1
    else :
        return x*factorial(x-1)
print (factorial.__doc__)
print("the factorial of 0 is",factorial(0))
print("the factorial of 1 is",factorial(1))
print("the factorial of 2 is",factorial(4))
print("the factorial of 5 is",factorial(5))
print("the factorial of 10 is",factorial(10))