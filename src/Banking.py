import random
import numpy as np
import pandas as pd
from scipy import stats
from tabulate import tabulate
from datetime import datetime,date
from Loan import Loan
from Customer import Customer
from Account import Account

class Banking:
    def __init__(self,data={}):
        customers=random.sample(['Jack','Jill','John','Joe','Jed','Jeff','Jess','Jim','Templeton','Hubert'],k=10)
        accounts=[111,123,222,333,444,555,666,777,888,999]
        balances=random.sample(list(-1*np.round(stats.uniform(0, 10000.0).rvs(20),2))
                        +list(np.round(stats.uniform(0, 1000000.0).rvs(100),2)),k=10)
        principals=random.sample([0,0,0,0,0]+list(np.round(stats.uniform(0, 1000000.0).rvs(5),0)),k=10)
        randates=[]
        for i in range(10):
            rdate=datetime.today() + (datetime(2024,1,1)-datetime.today()) * random.random()
            randates.append(str(rdate.date()))
        dfdata = pd.DataFrame({'cname':customers,'accountid':accounts,'balance':balances,'loan_outstanding':principals,'loan_deadline':randates})
        dfdata.loc[dfdata['loan_outstanding']==0,'loan_deadline']='N/A'
        self.data = dfdata.to_dict('list')
        print("Here some dummy data to reference while you enter new data:\n")
        print(tabulate(dfdata, headers='keys', tablefmt='psql', floatfmt='.2f',showindex=False))

    def transact(self):
        c = Customer()
        c.name = input('Please enter name: ')
        purpose = input('Enter "A" for ATM (Deposits/Withdrawals) or "T" for Teller (Loans)\n')
        if purpose == "A":
            c.accountid = input('Please enter account id: ')
            a = Account()
            a.accountid = c.accountid
            a.balance = float(input('Please how much money you want to play with: '))
            while True:
                session = c.visit_atm()
                if session == 'g':
                    print('Current Balance = $'+str(a.balance))
                elif session == 'd':
                    amount = input('How much would you like to deposit?')
                    a.deposit(amount)
                elif session == 'w':
                    amount = input('How much would you like to withdraw?')
                    a.withdraw(amount)
                elif session == 'e':
                    break
            b.data['cname'].append(c.name)
            b.data['accountid'].append(a.accountid)
            b.data['balance'].append(a.balance)
            b.data['loan_outstanding'].append(0.0)
            b.data['loan_deadline'].append('N/A')
        elif purpose == "T":
            c.accountid = input('Please enter account id: ')
            l = Loan()
            l.accountid = c.accountid
            l.repayDue = float(input('Please verify your outstanding amount due: '))
            strdate = input('Please verify your repayment deadline date (YYYY-MM-DD): ')
            l.repayDate = datetime.strptime(strdate, '%Y-%m-%d').date()
            while True:
                session = c.visit_teller()
                if session == 'm':
                    print(f'Prior to payment, loan outstanding: $%s , deadline: %s' %(l.repayDue,l.repayDate))
                    l.payMin()
                    print(f'Monthly minimum (total_amount/months_remaining) paid. Remaining outstanding: $%s'  %l.repayDue)
                elif session == 't':
                    l.payTotal()
                    print(f'Loan paid off in full! Remaining outstanding: $%s'  %l.repayDue)
                elif session == 'e':
                    break
            b.data['cname'].append(c.name)
            b.data['accountid'].append(l.accountid)
            b.data['balance'].append(0.0)
            b.data['loan_outstanding'].append(l.repayDue)
            b.data['loan_deadline'].append(l.repayDate)
        print("\nUpdated bank database after visit:\n")
        print(tabulate(pd.DataFrame(b.data), headers='keys', tablefmt='psql',floatfmt='.2f', showindex=False))
        print('\nHave a nice day...')

if __name__ == "__main__":
    b = Banking()
    b.transact()
