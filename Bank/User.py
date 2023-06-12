class User:

    # This function is our constructor, it creates the object for us
    def __init__(self, firstName, lastName, age, accountNumber, accountBalance, username, password):
        self.firstName = firstName
        self.lastName = lastName
        self.age = age
        self.accountNumber = accountNumber
        self.accountBalace = accountBalance
        self.username = username
        self.password = password

    # Getters and Setters. These functions get values and can change values for us

    def getName(self):
        fullName = self.firstName + self.lastName
        return fullName
    
    def setFirstName(self, newFirstName):
        self.firstName = newFirstName

    def setLastName(self, newLastName):
        self.lastName = newLastName

    def getAge(self):
        return self.age
    
    def setAge(self, newAge):
        self.age = newAge

    def getAccountNumber(self):
        return self.accountNumber
    
    def setAccountNumber(self, newAccountNumber):
        self.accountNumber = newAccountNumber

    def getAccountBalance(self):
        return self.accountBalace
    
    def setAccountBalance(self, newAccountBalance):
        self.accountBalace = newAccountBalance

    def getUserName(self):
        return self.username
    
    def setUserName(self, newUserName):
        self.username = newUserName

    def getPassword(self):
        return self.password
    
    def setPassword(self, newPassword):
        self.password = newPassword


    # Additional functions
     
