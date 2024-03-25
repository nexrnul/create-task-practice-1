import os
dailyconsumption=[]
print("evaluate your daily consumption of water")
#measurement = input("enter preferred measurment: liters, plastic bottles, glasses")
#bottle   liter   glasses 
#16.9oz  33.814oz   8oz


#initially many problems with location at: x00q273123 (discuss error)
def daily():
    daynum = 0
    for i in range(0,7):
        daynum = daynum+1
        days = int(input("amount of water " + (str(daynum)) + "days ago:"))
        dailyconsumption.append(days)
        os.system('clear')
    print (dailyconsumption)

userconsumptionlist = daily()


print(userconsumptionlist)