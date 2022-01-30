class Customer:
    def __init__(self,c_name=None,c_accountid=None):
        self.name = c_name
        self.accountid = c_accountid

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, new_name):
        self._name = new_name

    @property
    def accountid(self):
        return self._accountid
    
    @accountid.setter
    def accountid(self, new_id):
        self._accountid = new_id

    def visit_atm(self):
        purpose = input('Would you like to [g]et balance, [d]eposit, [w]ithdraw, or [e]nd transaction?')
        while purpose not in ['g','d','w','e']:
            purpose = input('Invalid entry, try again')
        return purpose