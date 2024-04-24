import os
daily_consumption=[]
daily_xercise=[]
calc_consumption=[] 
calc_xercise=[]
reccomended_oz=[]

blue = '\033[94m'
bluue = '\033[96m'
red = '\033[91m'
yellow = '\033[93m'
green = '\033[92m'
bold = '\033[1m'
reset = '\033[0m'
msrs = {'liters':34, 'bottles':17, 'glasses':8}

def record_data(determination, prompt, list):
#data_list.clear()
    for i in range (1,8):
        entry = int(input(prompt + " " + determination + f' {i} days ago:'))
        list.append(entry)
        os.system('clear')

def segment_ii():
    print(blue + bold + "evaluate your daily consumption of water"+ reset)
    inpmsr = input(bluue+ bold+"enter your preffered liquid measurment (liters, bottles, or glasses): ")
    os.system('clear')

    record_data(inpmsr, "enter your", daily_consumption)
    record_data("", "enter the number hours of exercise/physical activity you underwent",daily_xercise)

    inpweight = int(input("enter your estimated body weight: "))
    os.system('clear')

    for i in daily_consumption:
        calc_consumption.append(i * msrs[inpmsr])

    for i in daily_xercise:
        calc_xercise.append(i * (60//30 * 12))

    for i in calc_xercise:
        reccomended_oz.append(inpweight//2+i)
    
    print(bold + blue + "your current average daily consumption is", calc_avrg(calc_consumption,inpmsr))
    print(bold + blue + "with an average physical activity of", calc_avrg(daily_xercise, inpmsr))
    print(bold + blue + "your water goal should be around", calc_avrg(reccomended_oz, inpmsr) + " every day")

def calc_avrg(list, inpmsr):
    avrg = sum(list)/len(list)
    rounded_avrg = round(avrg)
    rounded_input = round(rounded_avrg/msrs[inpmsr])
    severity= ''
    
    if (sum(reccomended_oz) / len(reccomended_oz)) *0.4 >= avrg:
        severity = red
    elif (sum(reccomended_oz) / len(reccomended_oz)) *0.7 >= avrg:
        severity = yellow
    else:
        severity = green
    if list == daily_xercise:
        return f'{rounded_avrg} hours,'
    else:    
        return f'{severity}{rounded_avrg} ounces{blue} (about {rounded_input} {inpmsr})'

segment_ii()
