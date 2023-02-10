import pandas as pd

data1 = pd.read_html("https://www.screener.in/company/ASIANPAINT/consolidated/", skiprows=0, header=0)[0]

for i in range(len(data1.columns)):




# print(len(data1.columns))
print(data1.columns)