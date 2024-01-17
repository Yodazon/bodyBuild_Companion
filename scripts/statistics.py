
def determineStatView() -> bool:
    stats = False
    while stats is False:
        #print('Would you like to take a look at your stats? Y/n')
        statInput = input('Would you like to take a look at your stats? Y/n').lower()
        if statInput == 'y':
            print("Great! Lets take a look")
            stats = True
        elif statInput =='n':
            print("Oh, that's unfortunate!")
            stats = True
        else:
            print('Try again!')
    return stats