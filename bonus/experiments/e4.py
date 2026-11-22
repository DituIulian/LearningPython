import csv

with open("weather.csv") as file:
    data = list(csv.reader(file))

print(data)

city = input("Enter a city: ")

for row in data[1:]:
    if row[0] == city:
        print(f"Temperature in {row[0]} is:", row[1])