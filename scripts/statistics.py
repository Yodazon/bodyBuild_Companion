
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
    if stat_check is True:
        print("Which stats would you like to check out?")
        print("Calories - 1")
        print("Sleep - 2")
        print("Weight - 3")
        stat_Choice = input("Please input the corresponding number to check the stat")
        