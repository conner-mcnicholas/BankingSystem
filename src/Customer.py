from tkinter.tix import Balloon
import Account

class Customer:
    def __init__(self,name,cid,aid,crat,bal):
        self.customer_name = name
        self.customer_id = cid
        self.account_id = aid
        self.credit_rating = crat
        self.balance = bal
    
    def visit(self):
        session = input('Would you like to [g]et balance, [d]eposit, or [w]ithdraw?')
        a = Account(self.aid,self.balance)
        if session == 'g':
            print('Current Balance = $'+str(self.balance))
        elif session == 'd':
            amount = input('How much would you like to deposit?')
            a.deposit(amount)
        elif session == 'w':
            amount = input('How much would you like to withdraw?')
            a.withdraw(amount)
