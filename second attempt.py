import os
dailyconsumption=[]
print("evaluate your daily consumption of water")
#measurement = input("enter preferred measurment: liters, plastic bottles, glasses")
#bottle   liter   glasses 
#16.9oz  33.814oz   8oz
d = int(input("enter number of days you can recall your consumption:"))
if d < 2:
    print("error")


def daily():
    daynum = 0
    for i in range(d):
        daynum = daynum+1
        days = int(input("amount of water " + (str(daynum)) + "days ago:"))
        dailyconsumption.append(days)
        os.system('clear')
    print (dailyconsumption)

#daily(measurement)
#def daily(prefmeasurement):

print(daily())
#def calculations 

#input("enter your daily consumption of water in liters for past 7 days")

