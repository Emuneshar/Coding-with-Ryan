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
    


print(division(2,0))