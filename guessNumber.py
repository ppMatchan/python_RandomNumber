#Let user guess random number between 1 and 20 in 6 times
import random

print('Hello, what your name?')
name = input()

print('Well, ' + name + ', I`m thinking number between 1 and 20')
secretNumber = random.randint(1, 20)
print('Take a guess')


for guessTaken in range(1,7):
    try:
        guessNum = int(input())
    except ValueError:
        print('Input number baka!')
        continue
    
    if guessNum < secretNumber :
        print('your guess is too low.')
    elif guessNum > secretNumber :
        print('your guess is too high.')
    else:
        break

if guessNum == secretNumber :
    print('Good job, ' + name + 'You guess my number in ' + str(guessTaken) + 'guesses!')
else:
    print('Nope. The number I was think of was ' + str(secretNumber))
