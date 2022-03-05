from datetime import datetime,date

class Loan:
    def __init__(self,a_loanid=None,a_repayDue=0):
        self.loanid = a_loanid
        self.repayDue = float(a_repayDue)

    @property
    def loanid(self):
        return self._loanid

    @loanid.setter
    def loanid(self, new_id):
        self._loanid = new_id

    @property
    def repayDue(self):
        return float(self._repayDue)

    @repayDue.setter
    def repayDue(self, new_repayDue):
        self._repayDue = float(new_repayDue)

    @property
    def repayDate(self):
        return(self._repayDate)

    @repayDate.setter
    def repayDate(self, new_repayDate):
        self._repayDate = (new_repayDate)

    def payMin(self):
        currdate = date.today()
        deadline = self._repayDate
        monthsleft = int((abs(deadline - currdate).days)/30.5)
        monthlymin = self._repayDue/monthsleft
        self.repayDue = int(self.repayDue - monthlymin)

    def payTotal(self):
        self.repayDue = 0
