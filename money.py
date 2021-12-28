
import pandas as pd
import os
import requests
import fredapi as fa


def Get_Fred_API_Key():
    with open('fredapikey.txt', 'r') as file:
        key = file.readline().strip()
    return key


"""
To do dev list:
Get API US Fed total assets as frequently as possible
Get API BOE total assets as frequently as possible
Get API ECB total assets as frequently as possible
Get API PBC total assets as frequently as possible
Use groupby to convert them all to the least frequent of the bunch
Create from these a sum at the same frequency of "World_Money_Supply"
import assets of interest(sp500, housing, bitcoin, etc)
allow user to have start and end dates of interest
plot the asset and the asset in total world money supply
"""

fred_api_key = Get_Fred_API_Key()
# US FED
print('Working US Fed...\n')
series = 'RESPPANWW'
stem = 'https://api.stlouisfed.org/fred/series'
fred_str = f'?series_id={series}&api_key={fred_api_key}'
fred = fa.Fred(api_key=fred_api_key)
fed_assets = fred.get_series('RESPPANWW')
Fed_Assets = fed_assets.to_frame()
Fed_Assets.reset_index(inplace=True, drop=False)
Fed_Assets.rename(columns={'index': 'Date', 0: 'MM$US'}, inplace=True)
print(Fed_Assets)


#
