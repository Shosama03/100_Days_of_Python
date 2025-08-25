#Import the required libraries.
from art import logo,vs
from game_data import data
import random
from os import system

#We need to print the Higher_Lower logo.
def celebrity(account):
    """Takes the input of any celebrity and returns name,description and country."""
    celebrity_name=account['name']
    celebrity_description=account['description']
    celebrity_country=account['country']
    return f"{celebrity_name}, a {celebrity_description}, from {celebrity_country}."


def check_answer(user_guess,first_followers,second_followers):
    """Takes the user's guess and checks if the user choosed the correct celebrity with more followers."""
    if first_followers > second_followers:
        return user_guess == "a"
    else:
        return user_guess == "b"

print(logo)
score=0
game_should_continue=True

second_celebrity=random.choice(data)



while game_should_continue:
    first_celebrity=second_celebrity
    second_celebrity=random.choice(data)
    
    if first_celebrity == second_celebrity:
        second_celebrity = random.choice(data)
        
    print(f"Compare A: {celebrity(first_celebrity)}.")
    print(vs)
    print(f"Against B: {celebrity(second_celebrity)}.")

    guess=input("Who has more followers? Type 'A' or 'B' :").lower()
    system('cls')
    print(logo)


    first_follower_count=first_celebrity['follower_count']
    second_follower_count=second_celebrity['follower_count']


    is_correct=check_answer(guess,first_follower_count,second_follower_count)


    if is_correct:
        score+=1
        print(f"You are right! Current score {score}")
    else:
        print(f"Sorry, that's wrong! Final score {score}")
        game_should_continue=False









