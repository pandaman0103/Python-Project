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
        self.miniprice = miniprice
        self.miniterm = miniterm
        self.R_year = R_year
        self.miniprice = 1000
        self.miniterm = 2
        self.R_year = 0.01

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
        self.miniprice = miniprice
        self.miniterm = miniterm
        self.R_year = R_year
        self.miniprice = 3000
        self.miniterm = 5
        self.R_year = 0.03
    def GetComRateL(self, t):
        return super(LongBond, self).GetComRate(t)


#import the pakage for plotting
import matplotlib.pyplot as plt

#write function "mindollar" to abstract the change of minimumal price with time
def mindollar(iniprice,t,r):
    x = iniprice*(1+r)**t
    return x

# fix the arrays of X axis and Y axis in order to plot
x = [t for t in range(101)]
y1 = [mindollar(1000,t,0.01) for t in range(101)]
y2 = [mindollar(3000,t,0.03) for t in range(101)]

plt.plot(x,y1)
plt.plot(x,y2)
plt.title('minimal price for different type of bonds')
plt.legend(['short term bond', 'long term bond'])
plt.show()




