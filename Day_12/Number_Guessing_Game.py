from random import randint
from os import system
from art import logo


EASY_LEVEL_TURNS=10
HARD_LEVEL_TURNS=5

def check_answer(user_guess,actual_answer,turns):
    if user_guess>actual_answer:
        print("Too high!")
        return turns-1
    elif actual_answer>user_guess:
        print("Too low!")
        return turns-1
    else:
        print(f"You guessed correct. The number was {actual_answer}")
    
    


def set_difficulty():
    difficulty_level=input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if difficulty_level == 'easy':
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS
    
    
    
def game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    #To make this easy or for testing purpose, we can use this print line below.
    #print(f"Pssst. The number i'm thinking of is: {choosen_number}")
    choosen_number=randint(1,100) 
    print(f"Pssst. The number i'm thinking of is: {choosen_number}")

    turns=set_difficulty()
    

    user_guess=0
    
    while user_guess!=choosen_number:
        print(f"You have {turns} attempts remaining to guess the number. ")
        user_guess=int(input("Make a guess: "))
        
        turns=check_answer(user_guess,choosen_number,turns)
        if turns==0:
            print("You've run out of guesses, you lose.")
            return
        elif user_guess!=choosen_number:
            print("Guess again. ")

game()
        
