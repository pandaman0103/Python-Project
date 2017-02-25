##############      Part III : Investors        ##########################
from random import randint
from PythonProject import mindollar, Bond
import math
import random
import pandas as pd
import os
import matplotlib.pyplot as plt

# IMPORT DATA
datapath = 'H:\\UT1\M2\S2\python for finance\project\Data'
filepath = os.path.join(datapath, "AAPL.csv")
AAPL_df = pd.read_csv(filepath, ";")[[0, 2]]
AAPL_df['Date'] = AAPL_df['Date'].astype('datetime64[ns]')


filepath = os.path.join(datapath, "AXP.csv")
AXP_df = pd.read_csv(filepath, ";")[[0, 2]]
AXP_df['Date'] = AXP_df['Date'].astype('datetime64[ns]')

filepath = os.path.join(datapath, "FDX.csv")
FDX_df = pd.read_csv(filepath, ";")[[0, 2]]
FDX_df['Date'] = FDX_df['Date'].astype('datetime64[ns]')

filepath = os.path.join(datapath, "GOOGL.csv")
GOOGL_df = pd.read_csv(filepath, ";")[[0, 2]]
GOOGL_df['Date'] = GOOGL_df['Date'].astype('datetime64[ns]')

filepath = os.path.join(datapath, "IBM.csv")
IBM_df = pd.read_csv(filepath, ";")[[0, 2]]
IBM_df['Date'] = IBM_df['Date'].astype('datetime64[ns]')

filepath = os.path.join(datapath, "KO.csv")
KO_df = pd.read_csv(filepath, ";")[[0, 2]]
KO_df['Date'] = KO_df['Date'].astype('datetime64[ns]')

filepath = os.path.join(datapath, "MS.csv")
MS_df = pd.read_csv(filepath, ";")[[0, 2]]
MS_df['Date'] = MS_df['Date'].astype('datetime64[ns]')

filepath = os.path.join(datapath, "NOK.csv")
NOK_df = pd.read_csv(filepath, ";")[[0, 2]]
NOK_df['Date'] = NOK_df['Date'].astype('datetime64[ns]')

filepath = os.path.join(datapath, "XOM.csv")
XOM_df = pd.read_csv(filepath, ";")[[0, 2]]
XOM_df['Date'] = XOM_df['Date'].astype('datetime64[ns]')

filepath = os.path.join(datapath, "YHOO.csv")
YHOO_df = pd.read_csv(filepath, ";")[[0, 2]]
YHOO_df['Date'] = YHOO_df['Date'].astype('datetime64[ns]')


class Investor(object):
    def __init__(self, Budget, mode, start):
        self.Budget = Budget
        self.mode = mode
        self.start = start


class D_Investor(Investor):
    def __init__(self, Budget, mode, start):
        self.Budget = Budget
        self.mode = mode
        self.start = start
        self.mode = 'Defensive'


class A_Investor(Investor):
    def __init__(self, Budget, mode, start):
        self.Budget = Budget
        self.mode = mode
        self.start = start
        self.mode = 'Aggressive'


class M_Investor(Investor):
    def __init__(self, Budget, mode, start):
        self.Budget = Budget
        self.mode = mode
        self.start = start
        self.mode = 'Mixed'


# short term bond and long term bond with the same term : 10 years,initial budget = 12000
budget = 12000
Shortbond = Bond(10, math.floor(budget / 1000) * 1000, 1000, 2, 0.01)
Longbond = Bond(10, math.floor(budget / 3000) * 3000, 3000, 5, 0.03)


def Invest(investortype, budget,i):

    ROW_SBOND = []
    ROW_LBOND = []
    ROW_STOCK = []
    ROW_MIXED = []

    if investortype == 'Defensive':
        if randint(0, 1) == 0:  # the investor will invest only in the short bond
            nb_SB = math.floor(budget / 1000)
            budget_SB = nb_SB * 1000
            nb_LB = 0
            budget_LB = 0
            budgetleft = budget - budget_SB

        else:
            nb_LB = math.floor(budget / 3000)
            budget_LB = nb_LB * 3000
            nb_SB = math.floor((budget - budget_LB) / 1000)
            budget_SB = nb_SB * 1000
            budgetleft = budget - budget_LB - budget_SB
        Defensive_df=pd.DataFrame({'nb_SB':nb_SB, 'budget_SB':budget_SB, 'nb_LB':nb_LB, 'budget_LB':budget_LB, 'budgetleft':budgetleft},index=['i'])
        # Defensive_df= Defensive_df.append(Defensive_df_new, ignore_index=True)
        return Defensive_df

    # elif investortype == 'Aggressive':
    #     budgetleft = budget
    #     nb_AAPL = 0
    #     nb_AXP = 0
    #     nb_FDX = 0
    #     nb_GOOGL = 0
    #     nb_IBM = 0
    #     nb_KO = 0
    #     nb_MS = 0
    #     nb_NOK = 0
    #     nb_XOM = 0
    #     nb_YHOO = 0
    #     amount_AAPL = 0
    #     amount_AXP = 0
    #     amount_FDX = 0
    #     amount_GOOGL = 0
    #     amount_IBM = 0
    #     amount_KO = 0
    #     amount_MS = 0
    #     amount_NOK = 0
    #     amount_XOM = 0
    #     amount_YHOO = 0
    #     while (budgetleft >= 100):
    #         pick_stock = random.choice(['AAPL', 'AXP', 'FDX', 'GOOGL', 'IBM', 'KO', 'MS', 'NOK', 'XOM', 'YHOO'])
    #         if pick_stock == 'AAPL':
    #             Price_stock = round(float(AAPL_df[AAPL_df['Date'] == '2005-01-03']['High']), 2)
    #             nb_stock = randint(0, math.floor(budget / Price_stock) * 0.5)
    #             budgetleft = budget - Price_stock * nb_stock
    #             nb_AAPL = nb_AAPL + nb_stock
    #             amount_AAPL = amount_AAPL + Price_stock * nb_stock
    #
    #         elif pick_stock == 'AXP':
    #             Price_stock = round(float(AXP_df[AXP_df['Date'] == '2005-01-03']['High']), 2)
    #             nb_stock = randint(0, math.floor(budget / Price_stock) * 0.5)
    #             budgetleft = budget - Price_stock * nb_stock
    #             nb_AXP = nb_AXP + nb_stock
    #             amount_AXP = amount_AXP + Price_stock * nb_stock
    #         elif pick_stock == 'FDX':
    #             Price_stock = round(float(FDX_df[FDX_df['Date'] == '2005-01-03']['High']), 2)
    #             nb_stock = randint(0, math.floor(budget / Price_stock) * 0.5)
    #             budgetleft = budget - Price_stock * nb_stock
    #             nb_FDX = nb_FDX + nb_stock
    #             amount_FDX = amount_FDX + Price_stock * nb_stock
    #         elif pick_stock == 'GOOGL':
    #             Price_stock = round(float(GOOGL_df[GOOGL_df['Date'] == '2005-01-03']['High']), 2)
    #             nb_stock = randint(0, math.floor(budget / Price_stock) * 0.5)
    #             budgetleft = budget - Price_stock * nb_stock
    #             nb_GOOGL = nb_GOOGL + nb_stock
    #             amount_GOOGL = amount_GOOGL + Price_stock * nb_stock
    #         elif pick_stock == 'IBM':
    #             Price_stock = round(float(IBM_df[IBM_df['Date'] == '2005-01-03']['High']), 2)
    #             nb_stock = randint(0, math.floor(budget / Price_stock) * 0.5)
    #             budgetleft = budget - Price_stock * nb_stock
    #             nb_IBM = nb_IBM + nb_stock
    #             amount_IBM = amount_IBM + Price_stock * nb_stock
    #         elif pick_stock == 'KO':
    #             Price_stock = round(float(KO_df[KO_df['Date'] == '2005-01-03']['High']), 2)
    #             nb_stock = randint(0, math.floor(budget / Price_stock) * 0.5)
    #             budgetleft = budget - Price_stock * nb_stock
    #             nb_KO = nb_KO + nb_stock
    #             amount_KO = amount_KO + Price_stock * nb_stock
    #         elif pick_stock == 'MS':
    #             Price_stock = round(float(MS_df[MS_df['Date'] == '2005-01-03']['High']), 2)
    #             nb_stock = randint(0, math.floor(budget / Price_stock) * 0.5)
    #             budgetleft = budget - Price_stock * nb_stock
    #             nb_MS = nb_MS + nb_stock
    #             amount_MS = amount_MS + Price_stock * nb_stock
    #         elif pick_stock == 'NOK':
    #             Price_stock = round(float(NOK_df[NOK_df['Date'] == '2005-01-03']['High']), 2)
    #             nb_stock = randint(0, math.floor(budget / Price_stock) * 0.5)
    #             budgetleft = budget - Price_stock * nb_stock
    #             nb_NOK = nb_NOK + nb_stock
    #             amount_NOK = amount_NOK + Price_stock * nb_stock
    #         elif pick_stock == 'XOM':
    #             Price_stock = round(float(XOM_df[XOM_df['Date'] == '2005-01-03']['High']), 2)
    #             nb_stock = randint(0, math.floor(budget / Price_stock) * 0.5)
    #             budgetleft = budget - Price_stock * nb_stock
    #             nb_XOM = nb_XOM + nb_stock
    #             amount_XOM = amount_XOM + Price_stock * nb_stock
    #         else:
    #             Price_stock = round(float(YHOO_df[YHOO_df['Date'] == '2005-01-03']['High']), 2)
    #             nb_stock = randint(0, math.floor(budget / Price_stock) * 0.5)
    #             budgetleft = budget - Price_stock * nb_stock
    #             nb_YHOO = nb_YHOO + nb_stock
    #             amount_YHOO = amount_YHOO + Price_stock * nb_stock
    #     ROW_STOCK = ROW_STOCK.set_value(i, nb_AAPL, amount_AAPL, nb_AXP, amount_AXP, nb_FDX, amount_FDX, nb_GOOGL,
    #                                     amount_GOOGL, nb_IBM, amount_IBM, nb_KO, amount_KO, nb_MS, amount_MS, nb_NOK,
    #                                     amount_NOK, nb_XOM, amount_XOM, nb_YHOO, amount_YHOO, budgetleft)
    #     return ROW_STOCK
    # else:
    #     if randint(0, 1) == 0:  # the situation that the investor chooses the bond
    #         if randint(0, 1) == 0:  # the situation that the investor chooses the short term bond
    #             nb_SB = math.floor(budget / 1000)
    #             budget_SB = nb_SB * 1000
    #             nb_LB = 0
    #             budget_LB = 0
    #             budgetleft = budget - budget_SB
    #         else:
    #             nb_LB = math.floor(budget / 3000)
    #             budget_LB = nb_LB * 3000
    #             nb_SB = math.floor((budget - budget_LB) / 1000)
    #             budget_SB = nb_SB * 1000
    #             budgetleft = budget - budget_LB - budget_SB
    #
    #     else:  # this situation that the investor chooses the stock
    #         budgetleft = budget
    #         nb_AAPL = 0
    #         nb_AXP = 0
    #         nb_FDX = 0
    #         nb_GOOGL = 0
    #         nb_IBM = 0
    #         nb_KO = 0
    #         nb_MS = 0
    #         nb_NOK = 0
    #         nb_XOM = 0
    #         nb_YHOO = 0
    #         amount_AAPL = 0
    #         amount_AXP = 0
    #         amount_FDX = 0
    #         amount_GOOGL = 0
    #         amount_IBM = 0
    #         amount_KO = 0
    #         amount_MS = 0
    #         amount_NOK = 0
    #         amount_XOM = 0
    #         amount_YHOO = 0
    #         while (budgetleft >= 1000):
    #             pick_stock = random.choice(['AAPL', 'AXP', 'FDX', 'GOOGL', 'IBM', 'KO', 'MS', 'NOK', 'XOM', 'YHOO'])
    #             if pick_stock == 'AAPL':
    #                 Price_stock = round(float(AAPL_df[AAPL_df['Date'] == '2005-01-03']['High']), 2)
    #                 nb_stock = randint(0, math.floor(budget / Price_stock) * 0.5)
    #                 budgetleft = budget - Price_stock * nb_stock
    #                 nb_AAPL = nb_AAPL + nb_stock
    #                 amount_AAPL = amount_AAPL + Price_stock * nb_stock
    #
    #             elif pick_stock == 'AXP':
    #                 Price_stock = round(float(AXP_df[AXP_df['Date'] == '2005-01-03']['High']), 2)
    #                 nb_stock = randint(0, math.floor(budget / Price_stock) * 0.5)
    #                 budgetleft = budget - Price_stock * nb_stock
    #                 nb_AXP = nb_AXP + nb_stock
    #                 amount_AXP = amount_AXP + Price_stock * nb_stock
    #             elif pick_stock == 'FDX':
    #                 Price_stock = round(float(FDX_df[FDX_df['Date'] == '2005-01-03']['High']), 2)
    #                 nb_stock = randint(0, math.floor(budget / Price_stock) * 0.5)
    #                 budgetleft = budget - Price_stock * nb_stock
    #                 nb_FDX = nb_FDX + nb_stock
    #                 amount_FDX = amount_FDX + Price_stock * nb_stock
    #             elif pick_stock == 'GOOGL':
    #                 Price_stock = round(float(GOOGL_df[GOOGL_df['Date'] == '2005-01-03']['High']), 2)
    #                 nb_stock = randint(0, math.floor(budget / Price_stock) * 0.5)
    #                 budgetleft = budget - Price_stock * nb_stock
    #                 nb_GOOGL = nb_GOOGL + nb_stock
    #                 amount_GOOGL = amount_GOOGL + Price_stock * nb_stock
    #             elif pick_stock == 'IBM':
    #                 Price_stock = round(float(IBM_df[IBM_df['Date'] == '2005-01-03']['High']), 2)
    #                 nb_stock = randint(0, math.floor(budget / Price_stock) * 0.5)
    #                 budgetleft = budget - Price_stock * nb_stock
    #                 nb_IBM = nb_IBM + nb_stock
    #                 amount_IBM = amount_IBM + Price_stock * nb_stock
    #             elif pick_stock == 'KO':
    #                 Price_stock = round(float(KO_df[KO_df['Date'] == '2005-01-03']['High']), 2)
    #                 nb_stock = randint(0, math.floor(budget / Price_stock) * 0.5)
    #                 budgetleft = budget - Price_stock * nb_stock
    #                 nb_KO = nb_KO + nb_stock
    #                 amount_KO = amount_KO + Price_stock * nb_stock
    #             elif pick_stock == 'MS':
    #                 Price_stock = round(float(MS_df[MS_df['Date'] == '2005-01-03']['High']), 2)
    #                 nb_stock = randint(0, math.floor(budget / Price_stock) * 0.5)
    #                 budgetleft = budget - Price_stock * nb_stock
    #                 nb_MS = nb_MS + nb_stock
    #                 amount_MS = amount_MS + Price_stock * nb_stock
    #             elif pick_stock == 'NOK':
    #                 Price_stock = round(float(NOK_df[NOK_df['Date'] == '2005-01-03']['High']), 2)
    #                 nb_stock = randint(0, math.floor(budget / Price_stock) * 0.5)
    #                 budgetleft = budget - Price_stock * nb_stock
    #                 nb_NOK = nb_NOK + nb_stock
    #                 amount_NOK = amount_NOK + Price_stock * nb_stock
    #             elif pick_stock == 'XOM':
    #                 Price_stock = round(float(XOM_df[XOM_df['Date'] == '2005-01-03']['High']), 2)
    #                 nb_stock = randint(0, math.floor(budget / Price_stock) * 0.5)
    #                 budgetleft = budget - Price_stock * nb_stock
    #                 nb_XOM = nb_XOM + nb_stock
    #                 amount_XOM = amount_XOM + Price_stock * nb_stock
    #             else:
    #                 Price_stock = round(float(YHOO_df[YHOO_df['Date'] == '2005-01-03']['High']), 2)
    #                 nb_stock = randint(0, math.floor(budget / Price_stock) * 0.5)
    #                 budgetleft = budget - Price_stock * nb_stock
    #                 nb_YHOO = nb_YHOO + nb_stock
    #                 amount_YHOO = amount_YHOO + Price_stock * nb_stock
    #     ROW_MIXED = ROW_MIXED.set_value(i, nb_SB, budget_SB, nb_LB, budget_LB, nb_LB, budget_LB, nb_LB, budget_LB,
    #                                     nb_AAPL, amount_AAPL,
    #                                     nb_AXP, amount_AXP, nb_FDX, amount_FDX, nb_GOOGL, amount_GOOGL, nb_IBM,
    #                                     amount_IBM, nb_KO,
    #                                     amount_KO, nb_MS, amount_MS, nb_NOK, amount_NOK, nb_XOM, amount_XOM, nb_YHOO,
    #                                     amount_YHOO,
    #                                     budgetleft)
    #     return ROW_MIXED


# test
Defensive_df = pd.DataFrame({'nb_SB':'', 'budget_SB':'', 'nb_LB':'', 'budget_LB':'', 'budgetleft':''},index=['0'])
for i in range(100):
    new = Invest('Defensive', 12000,i)
    Defensive_df=Defensive_df.append(new, ignore_index=True)
print(Defensive_df)



#plot
x = [t for t in range(10)]
y1 = [mindollar(12000,t,0.01) for t in range(10)]
y2 = [mindollar(12000,t,0.03) for t in range(10)]

plt.plot(x,y1)
plt.plot(x,y2)
plt.title('Payoff for different type of bonds')
plt.legend(['short term bond', 'long term bond'])
plt.show()
