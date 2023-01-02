#generate a number 1 to 10
from random import randint

def run_guess(guess, ans):
    if 0 < guess < 11:
        if guess == ans:
            print('you are genius as you gussed right number')
            return True
    else:
        print('it should be 1 to 10')
        return False

if __name__ == '__main__':
    ans = randint(1, 10)
    while True:
        try:
            print(ans)
            guess = int(input('guess a number 1~10: '))
            if (run_guess(guess, ans)):
                break
        except ValueError:
            print("please enter a number")
            continue
