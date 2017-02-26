# This file is to finish the Project of "python for finance" course.
# The group number is Lu Chengwei and Li Mingjun
# The whole project is divided by four parts

#import mudules which are used in our preject
import pandas as pd
import os
import datetime
import matplotlib.pyplot as plt
import glob
import math
import random
from random import randint
import numpy as np
###############################################################################################
############################    Part I : Short and longterm bonds    ##########################
###############################################################################################
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

# write function "mindollar" to abstract the change of minimal price with time
def mindollar(iniprice,t,r):
    x = iniprice*(1+r)**t
    return x

# fix the arrays of X axis and Y axis in order to plot
x = [t for t in range(100)]
y1 = [mindollar(1000,t,0.01) for t in range(100)]
y2 = [mindollar(3000,t,0.03) for t in range(100)]

plt.plot(x,y1)
plt.plot(x,y2)
plt.title('minimal price for different type of bonds')
plt.legend(['short term bond', 'long term bond'])
plt.show()

###################################################################################
##############################     part II : Stocks    ############################
###################################################################################

#IMPORT DATA
datapath = 'H:\\UT1\M2\S2\python for finance\project\Data'

list_df = list()

for files in glob.glob(os.path.join(datapath,"*.csv")):
        df = pd.read_csv(files,";")[[0,2]]
        df['Date'] = df['Date'].astype('datetime64[ns]')
        list_df.append(df)

list_stock_name = ["AAPL", "AXP", "FDX", "GOOGLE", "IBM", "KO", "MS", "NOK", "XOM", "YHOO"]

#Define the class 'Stock'
class Stock(object):
    def __init__(self, term, amount, name, number, date, price):
        self.term = term
        self.amount = amount
        self.name = name
        self.number = number
        self.date = date
        self.price = price
#define a funtion to calculate the stock return
def Price_Return_stock(startdate,enddate,name):
    a = datetime.datetime.strptime(startdate, '%Y-%m-%d')
    b = datetime.datetime.strptime(enddate, '%Y-%m-%d')
    for (index, name_stock) in enumerate(list_stock_name):
        if name_stock == name:
            name_df = list_df[index]
            break
        else:
            pass

    while a not in list(name_df['Date']):
        a -= datetime.timedelta(days=1)
    while b not in list(name_df['Date']):
        b -= datetime.timedelta(days=1)

    Price = round(float(name_df[name_df['Date']== a]['High']),2)
    Return = round(((float(name_df[name_df['Date']== b]['High']) - Price)/Price),2)
    return Price, Return

#plot prices of 10 stocks
for (index,df) in enumerate(list_df):
    plt.plot(df[[0]],df[[1]],label=list_stock_name[index])

plt.xlabel('Time')
plt.ylabel('Price')
plt.title('Prices of 10 stocks')
plt.legend()
plt.show()
###############################################################################################
#################################      Part III : Investors        ############################
###############################################################################################
class Investor(object):
    def __init__(self, Budget, mode, start):
        self.Budget = Budget
        self.mode = mode
        self.start = start

class D_Investor(Investor):
    def __init__(self, Budget,start):
        self.Budget = Budget
        self.start = start
        self.mode = 'Defensive'

class A_Investor(Investor):
    def __init__(self, Budget,start):
        self.Budget= Budget
        self.start = start
        self.mode = 'Aggressive'

class M_Investor(Investor):
    def __init__(self, Budget,  start):
        self.Budget = Budget
        self.start = start
        self.mode = 'Mixed'

#this function is to calculate the return of every investor depending on different types and terms
def Invest(investor,end_investment):
    enddate = datetime.datetime.strptime(end_investment, '%Y-%m-%d')
    startdate = datetime.datetime.strptime(investor.start, '%Y-%m-%d')
    while enddate not in list(list_df[0]['Date']):
        enddate -= datetime.timedelta(days=1)
    while startdate not in list(list_df[0]['Date']):
        startdate -= datetime.timedelta(days=1)

    if investor.mode == 'Defensive':
        if randint(0, 1) == 0:                 # the investor will invest only in the short bond
            nb_SB = math.floor(investor.Budget / 1000)
            nb_LB = 0

        else:
            nb_LB = math.floor(investor.Budget / 3000)
            budget_LB = nb_LB * 3000
            nb_SB = math.floor((investor.Budget - budget_LB) / 1000)

        return_defen = round(3000 * nb_LB * (1 + 0.03) ** math.floor((enddate - startdate).days/365+1) + 1000 * nb_SB * (1 + 0.01) ** math.floor((enddate - startdate).days/365+1), 2)

        return return_defen

    elif investor.mode == 'Aggressive':

        budgetleft = investor.Budget
        list_nb = [0]*10

        while budgetleft >= 100:

            pick_stock = random.choice(list_stock_name)

            for (index, name_stock) in enumerate(list_stock_name):
                if name_stock == pick_stock:
                    pick_df = list_df[index]

                    price_stock = round(float(pick_df[pick_df['Date'] == startdate]['High']), 2)
                    nb_stock = randint(0, math.floor(math.floor(budgetleft / price_stock) * 0.5))

                    budgetleft -= price_stock * nb_stock
                    list_nb[index] = list_nb[index] + nb_stock
                    break
                else:
                    pass

        return_stock = 0
        for i, nb_stock in enumerate(list_nb):

            price = round(float(list_df[i][list_df[i]['Date'] == enddate]['High']), 2)
            return_stock += nb_stock * price

        return_aggre= round(return_stock, 2)

        return return_aggre

    else:
        if randint(0, 1) == 0:             # the situation that the investor chooses the bond
            if randint(0, 1) == 0:         # the investor will invest only in the short bond
                nb_SB = math.floor(investor.Budget / 1000)
                nb_LB = 0

            else:
                nb_LB = math.floor(investor.Budget / 3000)
                budget_LB = nb_LB * 3000
                nb_SB = math.floor((investor.Budget - budget_LB) / 1000)

            return_mix = round(3000 * nb_LB * (1 + 0.03) ** math.floor((enddate - startdate).days / 365+1) + 1000 * nb_SB * (
                                1 + 0.01) ** math.floor((enddate - startdate).days / 365+1), 2)

            return return_mix

        else:  # this situation that the investor chooses the stock
            budgetleft = investor.Budget
            list_nb = [0] * 10

            while budgetleft >= 1000:

                pick_stock = random.choice(list_stock_name)

                for (index, name_stock) in enumerate(list_stock_name):
                    if name_stock == pick_stock:
                        pick_df = list_df[index]

                        Price_stock = round(float(pick_df[pick_df['Date'] == startdate]['High']), 2)
                        nb_stock = randint(0, math.floor(math.floor(budgetleft / Price_stock) * 0.5))

                        budgetleft -= Price_stock * nb_stock
                        list_nb[index] = list_nb[index] + nb_stock
                        break
                    else:
                        pass

            return_stock = 0
            for i, nb_stock in enumerate(list_nb):
                price = round(float(list_df[i][list_df[i]['Date'] == enddate]['High']), 2)
                return_stock += nb_stock * price

                return_mix = round(return_stock, 2)

            return return_mix

# using the previous function 1000 times for each type of investors and calculate the average return in the end of the term
Return_defen = [0]*1000
for i in range(1000):
    defen_investor = D_Investor(12000, "2005-01-03")
    Return_defen[i] = Invest(defen_investor,"2015-01-05")
Average_defen = math.floor(sum(Return_defen)/1000)

Return_aggre = [0]*1000
for i in range(1000):
    aggr_investor = A_Investor(12000,"2005-01-03")
    Return_aggre[i] = Invest(aggr_investor,"2015-01-05")
Average_aggre = math.floor(sum(Return_aggre)/1000)

Return_mix = [0]*1000
for i in range(1000):
    mix_investor = M_Investor(12000,"2005-01-03")
    Return_mix[i] = Invest(mix_investor,"2015-01-05")
Average_mix = math.floor(sum(Return_mix)/1000)

print(Average_defen,Average_aggre,Average_mix)

#plot the average return for different types of investors
#define a function to put the exact number above every bar in our graph
def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        plt.text(rect.get_x()+rect.get_width()/2., 1.03*height, "%s" % float(height))

plt.xlabel('types of investors')
plt.ylabel('return in the end of term')
plt.xticks((1,4,7),('Defensive','Aggressive','mixed'))
rect = plt.bar(left=(1,4,7),height=(Average_defen,Average_aggre,Average_mix),width=0.60,align='center',yerr=0.0000000001,edgecolor = 'white')
autolabel(rect)
plt.title('average return for investors after 10 years')
plt.show()

