import csv

with open('files/weather.csv','r') as file:
    data = list(csv.reader(file))

city = input("Enter city name: ")

for row in data[1:]:
    if row[0] == city:
        print(row[1])

