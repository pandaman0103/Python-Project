##############      Part III : Investors        ##########################
from random import randint
from PythonProject import mindollar, Bond
import math
import random
import pandas as pd
import os
import datetime
import matplotlib.pyplot as plt
import glob

import numpy as np

#IMPORT DATA
datapath = 'H:\\UT1\M2\S2\python for finance\project\Data'

list_df = list()

for files in glob.glob(os.path.join(datapath,"*.csv")):
        df = pd.read_csv(files,";")[[0,2]]
        df['Date'] = df['Date'].astype('datetime64[ns]')
        list_df.append(df)

list_stock_name = ["AAPL", "AXP", "FDX", "GOOGLE", "IBM", "KO", "MS", "NOK", "XOM", "YHOO"]

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

# short term bond and long term bond with the same term : 10 years,initial budget = 12000
budget = 12000

def Invest(investor,i):

    if investor.mode == 'Defensive':
        if randint(0, 1) == 0:                 # the investor will invest only in the short bond
            nb_SB = math.floor(investor.Budget / 1000)
            budget_SB = nb_SB * 1000
            nb_LB = 0
            budget_LB = 0
            budgetleft = investor.Budget - budget_SB

        else:
            nb_LB = math.floor(budget / 3000)
            budget_LB = nb_LB * 3000
            nb_SB = math.floor((investor.Budget - budget_LB) / 1000)
            budget_SB = nb_SB * 1000
            budgetleft = investor.Budget - budget_LB - budget_SB

        Defensive_df = pd.DataFrame({'nb_SB':nb_SB, 'nb_LB':nb_LB},index=['i'])

        return Defensive_df

    elif investor.mode == 'Aggressive':
        startdate = datetime.datetime.strptime(investor.start, '%Y-%m-%d')

        budgetleft = investor.Budget
        list_nb = [0]*10

        while (budgetleft >= 100):

            pick_stock = random.choice(list_stock_name)

            for (index, name_stock) in enumerate(list_stock_name):
                if name_stock == pick_stock:
                    pick_df = list_df[index]

                    Price_stock = round(float(pick_df[pick_df['Date'] == startdate]['High']), 2)
                    nb_stock = randint(0, math.floor(math.floor(budgetleft / Price_stock) * 0.5))

                    budgetleft = budgetleft - Price_stock * nb_stock
                    list_nb[index] = list_nb[index] + nb_stock
                    break
                else:
                    pass

        Aggressive_df = pd.DataFrame(
            {'nb_' + list_stock_name[0]: list_nb[0], 'nb_' + list_stock_name[1]: list_nb[1], 'nb_' + list_stock_name[2]: list_nb[2],
             'nb_' + list_stock_name[3]: list_nb[3], 'nb_' + list_stock_name[4]: list_nb[4],
             'nb_' + list_stock_name[5]: list_nb[5], 'nb_' + list_stock_name[6]: list_nb[6],
             'nb_' + list_stock_name[7]: list_nb[7], 'nb_' + list_stock_name[8]: list_nb[8],
             'nb_' + list_stock_name[9]: list_nb[9]}, index=['i'])

        return Aggressive_df

    else:
        if randint(0, 1) == 0:             # the situation that the investor chooses the bond
            if randint(0, 1) == 0:  # the investor will invest only in the short bond
                nb_SB = math.floor(investor.Budget / 1000)
                budget_SB = nb_SB * 1000
                nb_LB = 0
                budget_LB = 0
                budgetleft = investor.Budget - budget_SB

            else:
                nb_LB = math.floor(budget / 3000)
                budget_LB = nb_LB * 3000
                nb_SB = math.floor((investor.Budget - budget_LB) / 1000)
                budget_SB = nb_SB * 1000
                budgetleft = investor.Budget - budget_LB - budget_SB

            Mix_df = pd.DataFrame({'nb_SB': nb_SB,'nb_LB': nb_LB,
                                   'nb_' + list_stock_name[0]: 0, 'nb_' + list_stock_name[1]: 0,
                                   'nb_' + list_stock_name[2]:0, 'nb_' + list_stock_name[3]: 0,
                                   'nb_' + list_stock_name[4]: 0, 'nb_' + list_stock_name[5]: 0,
                                   'nb_' + list_stock_name[6]: 0,'nb_' + list_stock_name[7]: 0,
                                   'nb_' + list_stock_name[8]: 0,'nb_' + list_stock_name[9]: 0}, index=['i'])
            SB = Mix_df['nb_SB']
            LB = Mix_df['nb_LB']
            Mix_df.drop(labels=['nb_SB'], axis=1, inplace=True)
            Mix_df.drop(labels=['nb_LB'], axis=1, inplace=True)
            Mix_df.insert(0, 'nb_SB', SB)
            Mix_df.insert(0, 'nb_LB', LB)

            return Mix_df


        else:  # this situation that the investor chooses the stock
            startdate = datetime.datetime.strptime(investor.start, '%Y-%m-%d')

            budgetleft = investor.Budget
            list_nb = [0] * 10

            while (budgetleft >= 100):

                pick_stock = random.choice(list_stock_name)

                for (index, name_stock) in enumerate(list_stock_name):
                    if name_stock == pick_stock:
                        pick_df = list_df[index]

                        Price_stock = round(float(pick_df[pick_df['Date'] == startdate]['High']), 2)
                        nb_stock = randint(0, math.floor(math.floor(budgetleft / Price_stock) * 0.5))

                        budgetleft = budgetleft - Price_stock * nb_stock
                        list_nb[index] = list_nb[index] + nb_stock
                        break
                    else:
                        pass

            Mix_df = pd.DataFrame(
                {'nb_SB': 0,'nb_LB': 0,
                'nb_' + list_stock_name[0]: list_nb[0], 'nb_' + list_stock_name[1]: list_nb[1],
                 'nb_' + list_stock_name[2]: list_nb[2],
                 'nb_' + list_stock_name[3]: list_nb[3], 'nb_' + list_stock_name[4]: list_nb[4],
                 'nb_' + list_stock_name[5]: list_nb[5], 'nb_' + list_stock_name[6]: list_nb[6],
                 'nb_' + list_stock_name[7]: list_nb[7], 'nb_' + list_stock_name[8]: list_nb[8],
                 'nb_' + list_stock_name[9]: list_nb[9]}, index=['i'])
            SB = Mix_df['nb_SB']
            LB = Mix_df['nb_LB']
            Mix_df.drop(labels=['nb_SB'], axis=1, inplace=True)
            Mix_df.drop(labels=['nb_LB'], axis=1, inplace=True)
            Mix_df.insert(0, 'nb_SB', SB)
            Mix_df.insert(0, 'nb_LB', LB)

            return Mix_df

# test

Defensive_df = pd.DataFrame({'nb_SB':'', 'nb_LB':''},index=['0'])

for i in range(1000):
    defen_investor = D_Investor(12000, "2005-01-03")
    new_Defensive_df = Invest(defen_investor,i)
    Defensive_df=Defensive_df.append(new_Defensive_df, ignore_index=True)

print(Defensive_df)

Aggressive_df = pd.DataFrame(
            {'nb_' + list_stock_name[0]: "", 'nb_' + list_stock_name[1]: "", 'nb_' + list_stock_name[2]: "",
             'nb_' + list_stock_name[3]: "", 'nb_' + list_stock_name[4]: "",
             'nb_' + list_stock_name[5]: "", 'nb_' + list_stock_name[6]: "",
             'nb_' + list_stock_name[7]: "", 'nb_' + list_stock_name[8]: "",
             'nb_' + list_stock_name[9]: ""}, index=['0'])

for i in range(1000):
    aggr_investor = A_Investor(12000,"2005-01-03")
    new_Aggressive_df = Invest(aggr_investor,i)
    Aggressive_df = Aggressive_df.append(new_Aggressive_df, ignore_index=True)

print(Aggressive_df)

Mix_df = pd.DataFrame(
            {'nb_SB':'', 'nb_LB':'',
            'nb_' + list_stock_name[0]: "", 'nb_' + list_stock_name[1]: "", 'nb_' + list_stock_name[2]: "",
             'nb_' + list_stock_name[3]: "", 'nb_' + list_stock_name[4]: "",
             'nb_' + list_stock_name[5]: "", 'nb_' + list_stock_name[6]: "",
             'nb_' + list_stock_name[7]: "", 'nb_' + list_stock_name[8]: "",
             'nb_' + list_stock_name[9]: ""}, index=['0'])

SB = Mix_df['nb_SB']
LB = Mix_df['nb_LB']
Mix_df.drop(labels=['nb_SB'], axis=1, inplace=True)
Mix_df.drop(labels=['nb_LB'], axis=1, inplace=True)
Mix_df.insert(0, 'nb_SB', SB)
Mix_df.insert(0, 'nb_LB', LB)

for i in range(1000):
    mix_investor = M_Investor(12000,"2005-01-03")
    new_mix_df = Invest(mix_investor,i)
    Mix_df = Mix_df.append(new_mix_df, ignore_index=True)

print(Mix_df)

# plot
#For the defensive investors
Return_defen = [0]*1001
for i in range(1,1001):
        Return_defen[i] = round(3000 * Defensive_df.iloc[i,0] * (1+0.03)**10 + 1000 * Defensive_df.iloc[i,1] * (1+0.01)**10,2)
Average_defen = math.floor(sum(Return_defen)/1000)

# For the aggressive investors
enddate = '2015-02-13'
b = datetime.datetime.strptime(enddate, '%Y-%m-%d')

Return_aggre = [0]*1001
for i in range(1,1001):
    return_stock = 0
    for col in range(10):
        Price = round(float(list_df[col][list_df[col]['Date'] == b]['High']), 2)
        return_stock = return_stock + Aggressive_df.iloc[i,col] * Price

    Return_aggre[i]= round(return_stock,2)

Average_aggre = math.floor(sum(Return_aggre)/1000)

# For the mix
Return_mix = [0]*1001
for i in range(1,1001):

        Return_bond= round(3000 * Defensive_df.iloc[i,0] * (1+0.03)**10 + 1000 * Defensive_df.iloc[i,1] * (1+0.01)**10,2)

        return_stock = 0
        for col in range(2,12):
            Price = round(float(list_df[col-2][list_df[col-2]['Date'] == b]['High']), 2)
            return_stock = return_stock + Mix_df.iloc[i, col] * Price

        Return_mix[i] = round(return_stock+ Return_bond, 2)

Average_mix = math.floor(sum(Return_mix)/1000)



#plot the average payoff for different types of investors
#firstly,define a function to put the exact number above every bar in our graph
def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        plt.text(rect.get_x()+rect.get_width()/2., 1.03*height, "%s" % float(height))

plt.xlabel('types of investors')
plt.ylabel('payoff in the end of the term')
plt.xticks((1,4,7),('Defensive','Aggressive','mixed'))
rect = plt.bar(left=(1,4,7),height=(Average_defen,Average_aggre,Average_mix),width=0.60,align='center',yerr=0.0000000001,edgecolor = 'white')
autolabel(rect)
plt.title('average payoff for investors after 10 years')
plt.show()



