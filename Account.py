class Account:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.__balance = 0
    def getBalance(self):
        return self.__balance
    def setBalance(self, balance):
        self.__balance += balance
    def getDetails(self):
        return f"{self.__balance} has been added to {self.name}'s account"
account = Account("John", 22)
print(account.getBalance())
account.setBalance(100)
print(account.getBalance())
account.setBalance(1000000000000000)
print(account.getBalance())
print(account.getDetails())