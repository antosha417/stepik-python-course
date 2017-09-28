import pandas as pd


data = pd.read_csv('Crimes.csv')
crimes = {}
for i in range(len(data)):
    year = data['Date'][i][6:10]
    if year == '2015':
        if data['Primary Type'][i] in crimes:
            crimes[data['Primary Type'][i]] += 1
        else:
            crimes[data['Primary Type'][i]] = 1
print(crimes)

