#### change wd
import os

os.chdir('/home/user01/example_data')

###### read and print data
with open('weather.csv', 'r') as reader:
    data = reader.read()
    print data


##### read file line by line
with open('weather.csv', 'r') as reader:
    data2 = reader.readline()
    while data2:
        print data2
        data2 = reader.readline()

print 'it is over'
        

###### read file line by line and grab only ranifall column.
with open('weather.csv', 'r') as reader:
    data3 = reader.readline()
    rain = []
    for line in reader.readlines():
        r = line.strip().split(',')[-1]
        r = float(r) 
        rain.append(r)

print rain
