# with open("weather.csv") as f:
#     data = f.read().splitlines()
#
# print(data)

# import csv
#
# with open("weather.csv") as csv_file:
#     data = csv.reader(csv_file, delimiter=',')
#
#     print(type(data))

import pandas as pd
import math

data = pd.read_csv("weather.csv")
print(data.head())
print(type(data))

# temperature = data["temp"].to_list()
# print(temperature)
#
# avg_temperature = sum(temperature) / len(temperature)
# print(avg_temperature)
#
# print(data["temp"].mean())
# print(f"Maximum temperature: {data["temp"].max()}")
#
# print(data[data["temp"] == data["temp"].max()])

mon_temp = data[data['day'] == "Monday"].temp[0]
print(type(mon_temp))
print(f"Monday temperature: {mon_temp} Celcius")
print(f"Monday temperature: {mon_temp*1.8 + 32} Fahrenheit")
