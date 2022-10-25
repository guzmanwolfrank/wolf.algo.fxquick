import requests 
import pandas as pd
import numpy as np
import defs
import matplotlib.pyplot as plt 

session = requests.Session()

instrument = 'USD_JPY'
count = 10
granularity = 'D'

url = f"{defs.OANDA_URL}/instruments/{instrument}/candles"


# url

params= dict( 
    count = count, 
    granularity = granularity, 
    price = 'M'
             )


#print(params)


response = session.get(url, params=params, headers=defs.SECURE_HEADER)


print(response.status_code)

response.json()

data = response.json()

data.keys()

#print(data)

prices = ['mid']
ohlc = ['o', 'h','l', 'c']


#for price in prices:
    #for oh in ohlc:
        #print(f"{price}_{oh}")
        
        
data['candles'][0]['mid']['o']

our_data = []
for candle in data['candles']:
    if candle ['complete'] == False:
        continue
    new_dict = {}
    new_dict['time'] = candle['time']
    new_dict['volume'] = candle['volume']
    for price in prices:
        for oh in ohlc: 
            new_dict[f"{price}_{oh}"] = candle[price][oh]
    our_data.append(new_dict)
#print(our_data[0])


candles_df = pd.DataFrame.from_dict(our_data)

#print(candles_df)

ff_data = pd.read_csv("ff_calendar_thisweek.csv")

#Entire DataFrame: includes several countries, reports, projections and actual outcomes
df = pd.DataFrame(ff_data)

#From the entire DataFrame, we are only focusing on the following columns
newdf = df[['Title','Country','Date','Time','Impact']]

#Defines : Only chooses USD (American) News Reports
usd_new = newdf[newdf['Country'] == 'USD'] 

#Defines different impact news for USD
highimp_usd = usd_new[usd_new['Impact']== "High"]
medimp_usd = usd_new[usd_new['Impact']== "Medium"]
lowimp_usd = usd_new[usd_new['Impact']== "Low"]

#print(candles_df[['time','volume','mid_c']].head(10))

table = (candles_df[['time','mid_c']].head(10))

print(table)


xlab = 'Intraday Date'
ylab = 'Price'
title = 'USD/JPY'


plt.xlabel(xlab)
plt.ylabel(ylab)
plt.title(title)
plt.plot(table['mid_c'])


plt.show()


# made by Wolfrank :) with forexfactory.com csv
# Objective of Script:  To easily filter, find and print USD Upcoming Economic Reports
#link [https://tinyurl.com/ybn435j7] for (csv,ics,json,xml)! 

#visit link above and download CSV to project root file folder! 

#defines CSV data being read and imported from root folder.


#Print different events by impact while showing time and date and hiding Index value.
print(highimp_usd.to_string(index=False))
print('')
print(medimp_usd.to_string(index=False))
print('')
print(lowimp_usd.to_string(index=False))
