
import pandas as pd
import os
import requests
import fredapi as fa

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
