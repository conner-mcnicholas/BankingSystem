import random
import numpy as np
import pandas as pd
import random
from scipy import stats
from tabulate import tabulate
from Customer import Customer
from Account import Account

class Banking:
    def __init__(self,data={}):
        customers=random.sample(['Jack','Jill','John','Joe','Jed','Jeff','Jess','Jim','Templeton','Hubert'],k=10)
        accounts=[111,123,222,333,444,555,666,777,888,999]
        balances=random.sample(list(-1*np.round(stats.uniform(0, 10000.0).rvs(20),2))
                        +list(np.round(stats.uniform(0, 1000000.0).rvs(100),2)),k=10)
        self.data = {'cname':customers,
                'aid':accounts,
                'bal':balances}
        print("Here some dummy data to reference while you enter new data:\n")
        print(tabulate(pd.DataFrame(self.data), headers='keys', tablefmt='psql', floatfmt='.2f',showindex=False))

    def transact(self):
        c = Customer()
        c.name = input('Please enter name: ')
        c.accountid = input('Please enter account id: ')
        a = Account()
        a.accountid = c.accountid
        a.balance = float(input('Please how much money you want to play with: '))
        status = True
        while status:
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
        b.data['aid'].append(a.accountid)
        b.data['bal'].append(a.balance)
        print("\nUpdated bank database after visit:\n")
        print(tabulate(pd.DataFrame(b.data), headers='keys', tablefmt='psql',floatfmt='.2f', showindex=False))
        print('\nHave a nice day...')
            
if __name__ == "__main__":
    b = Banking()
    b.transact()
