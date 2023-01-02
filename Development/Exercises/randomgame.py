#generate a number 1 to 10
from random import randint


import sys
#pytans = randint(1, 10)


ans = randint(int(sys.argv[1]), int(sys.argv[2]))
# input from user ?
#guess = input('guess a number 1~10: ') # program will work with it

#check the input is b/w 1 to 10

while True:
    try:
        print(ans)
        guess = input('guess a number 1~10: ')
        if 0 < int(guess) < 11:
            #print('all good is here')
            if int(guess) == ans:
                print('you are genius as you gussed right number')
                break
        else:
            print('it should be 1 to 10')
    except ValueError:
        print("please enter a number")
        break
# check if number if right guess otherwsie ask again