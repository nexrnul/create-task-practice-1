import os
dailyconsumption=[]
dailyxercise=[]
reccomended_oz=[]
calc_consumption=[] 
calcxercise=[]

blue = '\033[94m'
bluue = '\033[96m'
red = '\033[91m'
yellow = '\033[93m'
green = '\033[92m'
bold = '\033[1m'
reset = '\033[0m'
week = range(0,7)
daynum = 0

def daily(determination):
    global daynum 
    daynum = daynum+1
    if daynum > 7:
         daynum = 1
    global innerr 
    innerr = input(determination + " " + (str(daynum)) + " days ago:")

def calcaverage(list):
    avrg = sum(list)/len(list)
    roundd_avrg = (round(avrg))
    roundd_input = (round(roundd_avrg/msrs[inpmsr]))
    severity = 0
    if sum(reccomended_oz)/len(reccomended_oz)*0.4 >= avrg:
        severity = red
    elif sum(reccomended_oz)/len(reccomended_oz)*0.7 >= avrg:
        severity = yellow
    else:
        severity = green
    if list is dailyxercise:
        return f'{roundd_avrg} hours,'
    else: 
        return f'{severity}{roundd_avrg} ounces{blue} (about {roundd_input} {inpmsr})'

print(blue + bold + "evaluate your daily consumption of water"+ reset)
inpmsr = input(bluue+ bold+"enter your preffered liquid measurment (liters, bottles, or glasses): ")
msrs = {'liters':34, 'bottles':17, 'glasses':8}
if inpmsr in msrs:
    preffmsr = inpmsr
else: print("incorrect spelling try again")

for i in week:
    (daily(inpmsr))
    dailyconsumption.append(innerr)
    os.system('clear')
for i in week:
    (daily("enter the number hours of exercise/physical activity you underwent(1, 2, 3, etc.) "))
    dailyxercise.append(int(innerr))
    os.system('clear')

inpweight= int(input("enter your estimated body weight: "))
os.system('clear')

def calculations(user_list, calc_list, formula):
    for u in user_list:
        S = int(u)
        calc_list.append(formula(S)) 

calculations(dailyconsumption, calc_consumption, lambda formula: formula * msrs[inpmsr])

calculations(dailyxercise, calcxercise, lambda formula: formula * (60//30 * 12))

calculations(calcxercise, reccomended_oz, lambda formula: inpweight//2+formula)

print(bold + blue + "your current average daily consumption is",(calcaverage(calc_consumption)))
print(bold + blue + "with an average physical activity of",(calcaverage(dailyxercise)))
print(bold + blue + "your water goal should be around",(calcaverage(reccomended_oz)), "every day")
print(dailyxercise)
print(calcxercise)
print(calc_consumption)
print(reccomended_oz)

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