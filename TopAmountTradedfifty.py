# This program is to analyse the most amount traded stock at a specific time , for eg If I want to 
# check the most amount traded stock I shall multiply price * volume and then compare it with nifty 100 stocks

from datetime import date
import pandas as pd
import numpy as np
import yfinance as yf
import os
from plyer import notification

CompanyNames = pd.read_csv('StockData/CompanyNames.csv')
TotalCompany = 0
CompanyDataList = os.listdir(os.getcwd()+"/StockData") 

def speak(audio):
       # This command is to change voice 
       # espeak -ven-us+f4 -s170 "6 new wireless networks found"
       
       # engine = pyttsx3.init('sapi5')
       # voices = engine.getProperty('voices') #getting details of current voice
       # engine.setProperty('voice', voice[0].id)

       os.system('espeak'+' "'+audio+'"')  

# speak("hello")

mainDataFrame = pd.DataFrame()

for Company in CompanyNames.iloc[:,0]:
    try:
        data = yf.download(tickers=Company,start=date.today(), interval='5m')
        CompanyPrice = data.iloc[21,3]
        CompanyVolume = data.iloc[21,5]
        Amount = int(CompanyVolume) * int(CompanyPrice)
        datafr = pd.DataFrame({"Company": [Company] , "Amount": [Amount]}) 
        mainDataFrame = mainDataFrame.append(datafr)
    except:
        pass
    
    # CompanyPrice = data.iloc[9,3]
    # CompanyVolume = data.iloc[9,5]
    # Amount = int(CompanyVolume) * int(CompanyPrice)
    # datafr = pd.DataFrame({"Company": [Company] , "Amount": [Amount]}) 
    # mainDataFrame = mainDataFrame.append(datafr)
    # print(mainDataFrame)

mainDataFrame.to_csv("TopAmount/VolPriceAmountResult11Pm.csv")