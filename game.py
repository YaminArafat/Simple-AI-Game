from glob import glob
from random import random


from random import randint
import re
def Computer():
    global currentValue
    multiplyNumber = input()
    currentValue *= multiplyNumber
    return 0;

def Human():
    global currentValue
    multiplyNumber = input()
    currentValue *= multiplyNumber
    return check()

def check():
    if(currentValue>= target):
        return True
    else:
        return False
def playAgain():
    global play
    choice = input()
    if(choice == 'y'or choice=='Y'):
        play = True
    else:
        play = False
    return
play = True
currentValue = 1
gameOver = False
while(play == True):
    while(gameOver== False):
        target = randint(10, 100)
        print(target)
        round = 1
        if(round%2):
            gameOver = Computer()
        else:
            gameOver = Human()
        round+=1
    playAgain()


