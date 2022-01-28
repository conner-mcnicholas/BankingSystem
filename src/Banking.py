import random
import numpy as np
import pandas as pd
import random
from scipy import stats
from tabulate import tabulate
import Customer

class Banking:
    def __init__(self,ledger):
        ind = random.randint(1,10)
        customer_name = ledger.iloc[ind].cname
        customer_id = ledger.iloc[ind].cid
        credit_rating = ledger.iloc[ind].crat
        balance = ledger.iloc[ind].bal
        account_id = ledger.iloc[ind].aid
        print('Welcome, ' + customer_name + '!')
        c = Customer(customer_name, customer_id, account_id, credit_rating,balance)

if __name__ == "__main__":
    customerids=['123abc','123fgk','123xyz','666abc','666fgk','777vwq','666xyz','999abc','999fgk','999xyz']
    customers=random.sample(['Jack','Jill','John','Joe','Jed','Jeff','Jess','Jim','Templeton','Hubert'],k=10)
    accounts=[111,123,222,333,444,555,666,777,888,999]
    rating=random.choices(['A','B','C','D','F'],k=10)
    balances=random.sample(list(-1*np.round(stats.uniform(0, 10000.0).rvs(20),2))
                       +list(np.round(stats.uniform(0, 1000000.0).rvs(100),2)),k=10)
    data = {'cid':customerids,
            'cname':customers,
            'aid':accounts,
            'crat':rating,
            'bal':balances}
    df_ledger = pd.DataFrame(data)

    print(tabulate(df_ledger, headers='keys', tablefmt='psql', showindex=False))


    b = Banking(df_ledger)
