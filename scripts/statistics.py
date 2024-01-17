
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
    if stat_check is True:
        print("Which stats would you like to check out?")
        
        for i in len(x):
            print(x[i])

        stat_Choice = int(input("Please input the corresponding number to check the stat"))
        check = False
        while check is False:
            if stat_Choice == 1:
                print("Activity it is!")
                check = True
                stats_return = True
            elif stat_Choice == 2:
                print("Sleep it is! zzz")s
                check = True
                stats_return = False
            elif stat_Choice == 3:
                print("Weight it is!")
                check = True
                stats_return = False
            else:
                print('Try again!')
