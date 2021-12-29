
import pandas as pd
import os
import requests
import fredapi as fa


def Get_Fred_API_Key():
    with open('fredapikey.txt', 'r') as file:
        key = file.readline().strip()
    return key


def Get_Fred_Series(series, name):
    stem = 'https://api.stlouisfed.org/fred/series'
    fred_str = f'?series_id={series}&api_key={fred_api_key}'
    asset_series = fred.get_series(series)
    df = asset_series.to_frame()
    df.reset_index(inplace=True, drop=False)
    df.rename(columns={'index': 'Date', 0: name}, inplace=True)
    return df


"""
To do dev list:
Get API BOE total assets as frequently as possible
Get API ECB total assets as frequently as possible
Get API PBC total assets as frequently as possible
Use groupby to convert them all to the least frequent of the bunch
Create from these a sum at the same frequency of "World_Money_Supply"
import assets of interest(sp500, housing, bitcoin, etc)
allow user to have start and end dates of interest
plot the asset and the asset in total world money supply
"""
months = {'Jan': '01', 'Feb': '02', 'Mar': '03', 'Apr': '04', 'May': '05',
          'Jun': '06', 'Jul': '07', 'Aug': '08', 'Sep': '09', 'Oct': '10', 'Nov': '11', 'Dec': '12'}

fred_api_key = Get_Fred_API_Key()
fred = fa.Fred(api_key=fred_api_key)


# US FED data is weekly
print('Working US Fed...\n')
series = 'RESPPANWW'
Fed_Assets = Get_Fred_Series(series, 'USFED')
print(Fed_Assets)

# ECB


# PBC


# BOE


boe_till_14 = pd.read_csv('boe_till_14.csv', sep=' ', names=['Day', 'Mon', 'Yr+data'])
boe_till_14['Yr+data'] = boe_till_14['Yr+data'].astype(int)
boe_till_14['Yr+data'] = boe_till_14['Yr+data'].astype(str)
boe_till_14['Yr'] = boe_till_14['Yr+data'].str[0:2]
boe_till_14['BOE'] = boe_till_14['Yr+data'].str[2:]
boe_till_14.drop('Yr+data', inplace=True, axis=1)
for idx, row in boe_till_14.iterrows():
    yr = int(boe_till_14.loc[idx, 'Yr'])
    if yr > 14:
        year = '19'+str(yr)
    else:
        year = '20'+str(yr)
    boe_till_14.loc[idx, 'Year'] = year
    day = str(boe_till_14.loc[idx, 'Day'])
    if len(day) == 1:
        day = '0'+day
    mon = str(boe_till_14.loc[idx, 'Mon'])
    mon = months.get(mon)
    boe_till_14.loc[idx, 'Year'] = f'{year}-{mon}-{day}'
boe_till_14.drop(['Day', 'Mon', 'Yr'], axis=1, inplace=True)
boe_till_14.rename(columns={'Year': 'Date'}, inplace=True)
boe_till_14 = boe_till_14[['Date', 'BOE']]
print(boe_till_14)

#

#
