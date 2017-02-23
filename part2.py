###############     part II : Stocks    ########################
##import modules
import pandas as pd
import matplotlib.pyplot as plt
import os

#IMPORT DATA
datapath = 'H:\\UT1\M2\S2\python for finance\project\Data'
filepath = os.path.join(datapath,"AAPL.csv")
AAPL_df = pd.read_csv(filepath,";")[[0,2]]
AAPL_df['Date'] = AAPL_df['Date'].astype('datetime64[ns]')

filepath = os.path.join(datapath,"AXP.csv")
AXP_df = pd.read_csv(filepath,";")[[0,2]]
AXP_df['Date'] = AXP_df['Date'].astype('datetime64[ns]')

filepath = os.path.join(datapath,"FDX.csv")
FDX_df = pd.read_csv(filepath,";")[[0,2]]
FDX_df['Date'] = FDX_df['Date'].astype('datetime64[ns]')

filepath = os.path.join(datapath,"GOOGL.csv")
GOOGL_df = pd.read_csv(filepath,";")[[0,2]]
GOOGL_df['Date'] = GOOGL_df['Date'].astype('datetime64[ns]')

filepath = os.path.join(datapath,"IBM.csv")
IBM_df = pd.read_csv(filepath,";")[[0,2]]
IBM_df['Date'] = IBM_df['Date'].astype('datetime64[ns]')

filepath = os.path.join(datapath,"KO.csv")
KO_df = pd.read_csv(filepath,";")[[0,2]]
KO_df['Date'] = KO_df['Date'].astype('datetime64[ns]')

filepath = os.path.join(datapath,"MS.csv")
MS_df = pd.read_csv(filepath,";")[[0,2]]
MS_df['Date'] = MS_df['Date'].astype('datetime64[ns]')

filepath = os.path.join(datapath,"NOK.csv")
NOK_df = pd.read_csv(filepath,";")[[0,2]]
NOK_df['Date'] = NOK_df['Date'].astype('datetime64[ns]')

filepath = os.path.join(datapath,"XOM.csv")
XOM_df = pd.read_csv(filepath,";")[[0,2]]
XOM_df['Date'] = XOM_df['Date'].astype('datetime64[ns]')

filepath = os.path.join(datapath,"YHOO.csv")
YHOO_df = pd.read_csv(filepath,";")[[0,2]]
YHOO_df['Date'] = YHOO_df['Date'].astype('datetime64[ns]')

#Define the class 'Stock'
class Stock(object):
    def __init__(self, term, amount, name, number, date, price):
        self.term = term
        self.amount = amount
        self.name = name
        self.number = number
        self.date = date
        self.price = price


import datetime

def Price_Return_stock(startdate,enddate,name):
    a = datetime.datetime.strptime(startdate, '%Y-%m-%d')
    b = datetime.datetime.strptime(enddate, '%Y-%m-%d')

    while a not in list(name['Date']):
        a = a - datetime.timedelta(days=1)
    while b not in list(name['Date']):
        b = b - datetime.timedelta(days=1)

    Price = round(float(name[name['Date']== a]['High']),2)
    Return = round(((float(name[name['Date']== b]['High']) - Price)/Price),2)
    return Price, Return


a=Price_Return_stock('2005-01-08','2005-01-11',AAPL_df)
print(a)



#plot

plt.plot(YHOO_df[[0]],YHOO_df[[1]],label="$YHOO$",color="r")
plt.plot(YHOO_df[[0]],AAPL_df[[1]],"b--",label="$AAPL$")
plt.plot(YHOO_df[[0]],AXP_df[[1]],label="$AXP$",color="g")
plt.plot(YHOO_df[[0]],FDX_df[[1]],label="$FDX$",color="c")
plt.plot(YHOO_df[[0]],GOOGL_df[[1]],"r--",label="$GOOGL$")
plt.plot(YHOO_df[[0]],IBM_df[[1]],"y--",label="$IBM$")
plt.plot(YHOO_df[[0]],KO_df[[1]],label="$KO$",color="k")
plt.plot(YHOO_df[[0]],NOK_df[[1]],label="$NOK$",color="y")
plt.plot(YHOO_df[[0]],MS_df[[1]],"k--",label="$MS$")
plt.plot(YHOO_df[[0]],XOM_df[[1]],label="$XOM$",color="b")
plt.xlabel('Time')
plt.ylabel('Price')
plt.title('Prices of 10 stocks')
plt.legend()
plt.show()



