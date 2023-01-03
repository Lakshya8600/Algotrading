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

for Company in CompanyNames.iloc[:,0]:
    try:
        data = yf.download(tickers=Company,start=date.today(), interval='1m')
        Timeopen = data.iloc[1,0]
        Timeclose = data.iloc[-1,3]
    except:
        pass
    

    percentchange = 0
    if Timeopen >= Timeclose:
        percentchange = ((Timeopen-Timeclose)/Timeclose)*100
    else:
        percentchange = ((Timeclose-Timeopen)/Timeopen)*100

    # print(data)
    # print(data.iloc[-8,0])
    # print(data.iloc[-1,3]
    f = open('result.txt', 'at')
    if percentchange > 0.7:
        f.write(Company)
        f.write("\n")
        f.write(str(percentchange))
        f.write("\n")
        f.write("\n")
        # notification.notify(title = Company,message=str(percentchange) ,timeout=2)
        speak(Company)
        print(Company)
        print(percentchange)

    f.close()