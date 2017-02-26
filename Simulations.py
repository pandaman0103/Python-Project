########################        part IV: Simulations        ########################
from PythonProject import Invest
from PythonProject import A_Investor,D_Investor,M_Investor
from PythonProject import Price_Return_stock
import math
import pandas as pd
import os
import matplotlib.pyplot as plt
import glob
import numpy as np

#IMPORT DATA
datapath = 'H:\\UT1\M2\S2\python for finance\project\Data'

list_df = list()

for files in glob.glob(os.path.join(datapath, "*.csv")):
        df = pd.read_csv(files, ";")[[0,2]]
        df['Date'] = df['Date'].astype('datetime64[ns]')
        list_df.append(df)

list_stock_name = ["AAPL", "AXP", "FDX", "GOOGLE", "IBM", "KO", "MS", "NOK", "XOM", "YHOO"]

#1)plot the means for every year in the given dataset (always going from 01/01 to 31/12)



#2) When the starting budgets is 120000
Return_defen = [0]*1000
for i in range(1000):
    defen_investor = D_Investor(120000, "2005-01-03")
    Return_defen[i] = Invest(defen_investor,"2015-01-05")
Average_defen = math.floor(sum(Return_defen)/1000)

Return_aggre = [0]*1000
for i in range(1000):
    aggr_investor = A_Investor(120000,"2005-01-03")
    Return_aggre[i] = Invest(aggr_investor,"2015-01-05")
Average_aggre = math.floor(sum(Return_aggre)/1000)

Return_mix = [0]*1000
for i in range(1000):
    mix_investor = M_Investor(120000,"2005-01-03")
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
plt.ylabel('payoff in the end of the term')
plt.xticks((1,4,7),('Defensive','Aggressive','mixed'))
rect = plt.bar(left=(1,4,7),height=(Average_defen,Average_aggre,Average_mix),width=0.60,align='center',yerr=0.0000000001,edgecolor = 'white')
autolabel(rect)
plt.title('average payoff for investors after 10 years')
plt.show()


#3)Starting budget randomly from a normal distribution centered around 20000 with a standard deviation of 5000
#In this exercise, we should check whether the minimal budget is larger than 1000. If the random number produced is larger than 1000, it's ok.Otherwise it should be an error warning.
budget = np.random.normal(20000,5000)

Return_defen = [0]*1000
for i in range(1000):
    defen_investor = D_Investor(budget, "2005-01-03")
    Return_defen[i] = Invest(defen_investor,"2015-01-05")
Average_defen = math.floor(sum(Return_defen)/1000)

Return_aggre = [0]*1000
for i in range(1000):
    aggr_investor = A_Investor(budget,"2005-01-03")
    Return_aggre[i] = Invest(aggr_investor,"2015-01-06")
Average_aggre = math.floor(sum(Return_aggre)/1000)

Return_mix = [0]*1000
for i in range(1000):
    mix_investor = M_Investor(budget,"2005-01-03")
    Return_mix[i] = Invest(mix_investor,"2015-01-06")
Average_mix = math.floor(sum(Return_mix)/1000)

print(Average_defen,Average_aggre,Average_mix)
#4)What was the best stock to have in 2007?
return_2007 = [0]*10
for index,name in enumerate(list_stock_name):
    return_2007[index]=Price_Return_stock('2007-01-03','2007-12-31',name)

print(list_stock_name[return_2007.index(max(return_2007))])

#5)what was on average the best year for an aggressive investor (always going from 01/01 to 31/12)
list_year = ["05","06","07","08","09","10","11","12","13","14","15"]
list_year_average = [0]*11
budget = 12000
for index,year in enumerate(list_year):
    Return_aggre = [0] * 1000
    for i in range(1000):
        aggr_investor = A_Investor(budget,"20%s-01-03"%list_year[index])
        Return_aggre[i] = Invest(aggr_investor,"20%s-12-31"%list_year[index])

    list_year_average[index] = math.floor(sum(Return_aggre)/1000)

print(list_year_average)
print(list_year[list_year_average.index(max(list_year_average))])

