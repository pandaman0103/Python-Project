# This file is to finish the Project of "python for finance" course.
# The group number is Lu Chengwei and Li Mingjun
# The whole project is divided by four parts

##################    The first part: Short and longterm bonds    ###############
#Firstly, create the bond as a class
class Bond(object):
    def __init__(self, term, amount, miniprice, miniterm, R_year):
        self.term = term
        self.amount = amount
        self.miniprice = miniprice
        self.miniterm = miniterm
        self.R_year = R_year
    def GetComRate(self, t):
        self.R_com = (1 + self.R_year)**t - 1
        return self.R_com
class ShortBond(Bond):
    def __init__(self, term, amount, miniprice, miniterm, R_year):
        if 2 <= term < 5:
            self.term = term
        else:
            raise ValueError('The term of short bond is from 2 years to 5 years (not included)')
        if amount > 1000:
            self.amount = amount
        else:
            raise ValueError('The minimum amount of short bond is $1000')
        self._miniprice = miniprice              # Having a underline before a variable can make the value of this variable be inchanged from the exterior.
        self._miniterm = miniterm
        self._R_year = R_year
    def GetComRateS(self, t):
        # super is up to the class before which is a object "Bond"
        return super(ShortBond, self).GetComRate(t)

class LongBond(Bond):
    def __init__(self, term, amount, miniprice, miniterm, R_year):
        if term >= 5:
            self.term = term
        else:
            raise ValueError('The term of long bond is more than 5 years (included)')
        if amount > 3000:
            self.amount = amount
        else:
            raise ValueError('The minimum amount of short bond is $3000')
        if miniprice != 1000:
            self._miniprice = 1000
        else:
            raise ValueError('The minimum amount of short bond is $3000')
        self._miniterm = miniterm
        self._R_year = R_year
    def GetComRateL(self, t):
        return super(LongBond, self).GetComRate(t)

Sbond1 = ShortBond(3,2000)
print(Sbond1.R_year)