class Account:
    def __init__(self, defaultPin='1234', defaultBalance=10000):
        self.pin = defaultPin
        self.balance = defaultBalance

    def checkPin(self, pin):
        if self.pin == pin:
            return True
        else:
            return False

    def getBalance(self):
        return self.balance

    def withdraw(self, amount):
        self.balance -= amount

    def topup(self, amount):
        self.balance += amount

    def changePin(self, newPin):
        self.pin = newPin
