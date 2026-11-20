import csv

with open("weather.csv") as file:
    data = list(csv.reader(file))

print(data)