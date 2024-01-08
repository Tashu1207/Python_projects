from art import logo
import os
import random
def welcome():
    os.system('cls')
    print(logo)
    print("Welcome to the Number guessing game!")
    print("I am guessing a number between : 1 and 100")

def choose_dificulty():
    dificulty = input("Choose the dificulty, 'easy' or 'hard':")
    return dificulty

def check(gussed_num):
    global chances
    if gussed_num == number:
        chances = -1
        print(f"you got it, the number was {number}")
    elif gussed_num > number:
        print("Too high!\nGuess again")
    elif gussed_num < number:
        print("Too low\nGuess again")
       
def guess_number():
    
    print(f"You have {chances} attempts remaining to guess the number.")
    gussed_num = int(input("Make a guess:"))
    check(gussed_num)


while input("do you want to play the game, to play type 'y' ") =='y':
    welcome()
    number = random.randint(1,100)
    print(number)
    dificulty =choose_dificulty()
    if dificulty == "hard":
        chances = 5
    elif dificulty == "easy":
        chances = 10
    else:
        print("invalid input")

    while chances > 0:
        guess_number()
        chances -= 1
    
    if chances == 0:
        print("You ran out of Guesses, You lose")




