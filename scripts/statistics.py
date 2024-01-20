import numpy as numpy
import matplotlib.pyplot as plt
import pandas as pd




def determineStatView() -> bool:
    check = False
    while check is False:
        #print('Would you like to take a look at your stats? Y/n')
        statInput = input('Would you like to take a look at your stats? Y/n').lower()
        if statInput == 'y':
            print("Great! Lets take a look")
            check = True
            stats_return = True
        elif statInput =='n':
            print("Oh, that's unfortunate!")
            check = True
            stats_return = False
        else:
            print('Try again!')
    return stats_return


def statCheck(stat_check):
    x = ["Activity (Steps, Calories) - 1",
         "Sleep - 2",
         "Weight - 3"
         ]
    y = ["Activity it is!",
         "Sleep it is! zzz",
         "Weight it is!",
         'Try again!']
    if stat_check is True:
        print("Which stats would you like to check out?")
        
        for i in range(len(x)):
            print(x[i])

        stat_Choice = int(input("Please input the corresponding number to check the stat"))
        check = False
        while check is False:
            if stat_Choice == 1:
                print(y[0])
                check = True
                stats_return = True
            elif stat_Choice == 2:
                print(y[1])
                check = True
                stats_return = False
            elif stat_Choice == 3:
                print(y[2])
                check = True
                stats_return = False
            else:
                print(y[3])

        showStat(stat_Choice)


def showStat(stat_Choice):
    adjusted_Stat_Choice = stat_Choice -1 
    stat = ['activity.csv',
            "sleep.csv",
            "weight.csv"]
    print(f"Cool, lets take a look at {stat[adjusted_Stat_Choice]}")

    plotStat(stat[adjusted_Stat_Choice], adjusted_Stat_Choice)

def plotStat(stat, stat_Choice):
    print (stat)
    ##The following path is for the computer
    csv_path = "C:\\Coding\\Github\\bodyBuild_Companion\\data" + stat

    df_Plot_Stat = pd.read_csv(csv_path)

    if stat_Choice == 1:
        df_Plot_Stat.plot(x = "Activity Date", y = "Total Steps", kind ="line" )
    elif stat_Choice == 2:
        df_Plot_Stat.plot(x = "Sleep Day", y = "Total Minutes Asleep", kind ="line" )
    else:
        df_Plot_Stat.plot(x = "Date", y = "Weight Pounds", kind ="line" )

    

