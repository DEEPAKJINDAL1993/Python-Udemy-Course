import pandas as pd

data = pd.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20241009.csv')

print(data.columns)

data_color = data.agg('count', data["Primary Fur Color"])
print(data_color)