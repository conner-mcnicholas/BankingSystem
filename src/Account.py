class Account:
    def __init__(self,a_accountid=None,a_balance=0):
        self.accountid = a_accountid
        self.balance = float(a_balance)

    @property
    def accountid(self):
        return self._accountid
    
    @accountid.setter
    def accountid(self, new_id):
        self._accountid = new_id

    @property
    def balance(self):
        return float(self._balance)

    @balance.setter
    def balance(self, new_balance):
        self._balance = float(new_balance)

    def deposit(self,amount=0):
        amount = float(amount)
        if amount == '':
            amount = 0.0
        self.balance = self.balance + float(amount)

    def withdraw(self,amount=0):
        amount = float(amount)
        if amount == '':
            amount = 0.0
        if(self.balance - amount) < 0:
            print('Not enough funds!')
        else:
            self.balance = self.balance - amount
