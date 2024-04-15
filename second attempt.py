import os
dailyconsumption=[]
dailyxercise=[]
reccomended_oz=[]
blue = '\033[94m'
bluue = '\033[96m'
red = '\033[91m'
yellow = '\033[93m'
green = '\033[92m'
bold = '\033[1m'
reset = '\033[0m'
week = range(0,7)
daynum = 0

def daily(console, determination):
    global daynum 
    daynum = daynum+1
    if daynum > 7:
         daynum = 1
    global innerr 
    innerr = int(console(determination + " " + (str(daynum)) + " days ago:"))

def calcaverage(list):
    avrg = sum(list)/len(list)
    roundd_avrg = (round(avrg))
    roundd_input = (round(roundd_avrg/msrs[inpmsr]))
    severity = 0
    if sum(reccomended_oz)/len(reccomended_oz)*0.7 >= avrg:
        severity = yellow
    elif sum(reccomended_oz)/len(reccomended_oz)*0.4 >= avrg:
        severity = red
    else:
        severity = green
    if list is dailyxercise:
        return f'{roundd_avrg} hours,'
    else: 
        return f'{severity}{roundd_avrg} ounces{blue} (about {roundd_input} {inpmsr})'

print(blue + bold + "evaluate your daily consumption of water"+ reset)
inpmsr = str(input(bluue+ bold+"enter your preffered liquid measurment (liters, bottles, or glasses): "))
msrs = {'liters':34, 'bottles':17, 'glasses':8}
if inpmsr in msrs:
    preffmsr = inpmsr
else: print("incorrect spelling try again")

for i in week:
    (daily(input, inpmsr))
    dailyconsumption.append(innerr)
    os.system('clear')
for i in week:
    (daily(input, ((("enter the number hours of exercise/physical activity you underwent(1, 2, 3, etc.) ")))))
    dailyxercise.append(innerr)
    os.system('clear')

inpweight= int(input("enter your estimated body weight: "))
os.system('clear')

#DONT IGNORE ------ def calculatio`lns(weight, activity):
calc_consumption=[] 
for M in dailyconsumption:
    O = int(M)
    calc_consumption.append(M * msrs[inpmsr])    

calcxercise=[]
for L in dailyxercise:
    i = int(L)
    calcxercise.append(i * 60//30 * 12)
    
for i in calcxercise:
    weightcalc= inpweight//2 
    reccomended_oz.append(weightcalc + i) 

print(bold + blue + "your current average daily consumption is",(calcaverage(calc_consumption)))
print(bold + blue + "with an average physical activity of",(calcaverage(dailyxercise)))
print(bold + blue + "your water goal should be around",(calcaverage(reccomended_oz)), "every day")
#print(calcxercise)
#print(calc_consumption)
#print(reccomended_oz)

#average water consumed past week
#average water consumption goal for week
#average hours exercised per week
#average hours exercised a day in week?

#initially many problems with location at: x00q273123 (discuss error)
#MANY problems with int, str not being callable// some other err along those lines


#while inpmsr != msrs:
#while inpmsr != key in msrs.keys():
 #   input(inpmsr)
        #input(inpmsr)
#preffmsr = inpmsr:

#bottle   liter   glasses 
#16.9oz  33.814oz   8oz
#if inpmsr in msrs:
#    preffmsr = inpmsr
#else: print("incorrect spelling try again") 