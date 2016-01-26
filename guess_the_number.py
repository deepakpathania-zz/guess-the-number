import math
import random

#initializing the globals
attempts=7
correct=0

#restarts the game based on user input
def newgame():
    global attempts
    print " "
    i =  int(raw_input(" Do you want to continue playing  1/0 ? "))
    if i==1:
        attempts=7
        global correct
        correct=correct_ans()
        choose_number()
    else :
        exit()

#selects a random answer between 0 and 100
def correct_ans():
    correct=random.randint(0,101)
    return correct

correct=correct_ans()

#main game logic, prompts the user about deviation from answer while decrementing attempts
def input_guess(guess):
    global attempts,correct
    if attempts==1 and guess!=correct:
        print "You lost"
        newgame()
    if guess==correct:
        print "You got it right : " ,guess
        newgame()
    elif guess<correct:
        print "Try higher"
        attempts-=1
        print "Attempts left : ",attempts
        choose_number()
    else :
        print " Try lower"
        attempts-=1
        print "Attempts left : ",attempts
        choose_number()
        

print  "Welcome to guess the number "

#prompts the user to enter a number on each turn
def choose_number():
    t=int(raw_input("Start guessing : ")) 
    input_guess(t)

#starts the game
choose_number()
