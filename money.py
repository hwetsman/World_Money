
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
Get API BOE total assets since 2014 as frequently as possible
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
# The BOE doesn't have an API and is very slow as a website
# get BOE data until 2014 from saved csv
boe_till_14 = pd.read_csv('boe_till_14.csv')

print(boe_till_14)
#

#
