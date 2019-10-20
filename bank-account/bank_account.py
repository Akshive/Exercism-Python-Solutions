from threading import Lock

class Custom_Exception(Exception):
    pass

class BankAccount(object):
    def __init__(self):
        self.IsOpen = False
        self.Balance = 0

    def get_balance(self):
        if(self.IsOpen == False):
            raise ValueError('Invalid args.')
        return self.Balance

    def open(self):
        if(self.IsOpen == True):
            raise ValueError('Invalid args.')
        self.IsOpen = True

    def deposit(self, amount):
        lock = Lock()
        lock.acquire()
        try:
            if(amount < 0 or self.IsOpen == False):
                raise ValueError('Invalid args.')
            self.Balance += amount
        finally:
            lock.release()

    def withdraw(self, amount):
        lock = Lock()
        lock.acquire()
        try:
            if(amount < 0 or self.IsOpen == False or amount > self.Balance):
                raise ValueError('Invalid args.')
            self.Balance -= amount
        finally:
            lock.release()

    def close(self):
        if(self.IsOpen == False):
            raise ValueError('Invalid args.')
        self.Balance = 0
        self.IsOpen = False
