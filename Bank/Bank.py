import random
import User


print("Welcome to The Coach Bank")

print("You have the following options\n",
      "1. Open an Account\n",
      "2. Withdraw Money\n",
      "3. Deposit Money\n",
      "4. View account balance\n",
      "5. Close Account\n"
      )

choice = int(input("Which one would you like?"))


def openAccount():
    print("Thank you for openening an account\n")
    print("In order to open an account for you we will need to get some information\n")
    fName = str(input("What is your first name?\n"))
    lName = str(input("What is your last name\n"))
    age = int(input("How old are you?\n"))
    accountNum = random.randint(9999999, 99999999999)
    accountBal = int(input("Enter the amount of money that you would like to put into your account\n"))
    userName = str(input("Please create a username for your account\n"))
    password = str(input("Please enter a password\n"))
    print("Your account number is ", accountNum, "Please wait while we create your account")
    person = User(fName, lName, age, accountNum, accountBal, userName, password)
    return person


match choice:
    case 1:
        openAccount()

