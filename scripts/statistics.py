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

#
#StatCheck and showStat is deprecated due to the involvement of a frontend HTML with Flask Backend
#Jan 22, 2024
'''
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

    # Deprecated, no longer needed with using flask
    #adjusted_Stat_Choice = stat_Choice -1 

    stat = ['activity.csv',
            "sleep.csv",
            "weight.csv"]
    print(f"Cool, lets take a look at {stat[stat_Choice]}")

    plot = plotStat(stat[stat_Choice], stat_Choice)
    return (plot)
'''

def plotStat(value):
    stat = ['activity.csv',
            "sleep.csv",
            "weight.csv"]
    ##The following path is for the computer
    csv_path = "C:\\Coding\\Github\\bodyBuild_Companion\\data\\" + stat[value]

    df_Plot_Stat = pd.read_csv(csv_path)

    if value == 0:
        figure = df_Plot_Stat.plot(x = "ActivityDate", y = "TotalSteps", kind ="line" )
    elif value == 1:
        figure = df_Plot_Stat.plot(x = "SleepDay", y = "TotalMinutesAsleep", kind ="line" )
    else:
        figure = df_Plot_Stat.plot(x = "Date", y = "WeightPounds", kind ="line" )

    folder_path = 'C:\\Coding\\Github\\bodyBuild_Companion\\app\\generatedStats\\'
    figure_name = 'figure.jpg'
    file_path = folder_path + figure_name


    fig = figure.get_figure() 
    fig.savefig(file_path)

    return (file_path)



    

