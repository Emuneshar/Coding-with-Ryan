# def is short for define

# Parameters are variables from the code that we want our function to have access to

# Return - returns the result from our function

def evenOrOdd(number):
    if number % 2 == 1:
        print("odd")
    else:
        print("even")

def addition(numOne, numTwo):
    return numOne+numTwo

def subtraction(numOne, numTwo):
    return numOne-numTwo

def division(numOne, numTwo):
    if numTwo == 0:
        return "You cannot divide by 0"
    else:
        return numOne/numTwo
    

numOne = int(input("What is the first number?"))
numTwo = int(input("What is the second number"))

operation = input("What would you like to do? Your options are addition, subtraction, multiplication, division and parity")

# you can use if else
if operation == "addition":
    print(addition(numOne, numTwo))

# The other option is to use something called match and case
