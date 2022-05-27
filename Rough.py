from datetime import date
import pandas as pd
import numpy as np
import yfinance as yf
from matplotlib import pyplot as plt
import os
from string import digits

data = yf.download(tickers="RELIANCE.NS",start="2022-03-28", interval='2m',index=True)
# data.to_csv("DataAnalysis.csv")
# str = str(data.index[0])
# print(str[11:13])