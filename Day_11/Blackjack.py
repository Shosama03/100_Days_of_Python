import random
from os import system
from art import logo,win,lose,draw
def deal_cards():
    """Returns a random card from the deck of cards."""
    deck=[11,2,3,4,5,6,7,8,9,10,10,10,10]
    draw_from_deck=random.choice(deck)
    return draw_from_deck

def calculate_score(cards):
    """Takes a list of cards as input and returns the score."""
    if sum(cards)==21 and len(cards)==2:
        return 0
    
    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)
        
    return sum(cards)

def compare(u_score,c_score):
    if u_score==c_score:
        print(draw)
        return "Draw!!!"
    elif c_score==0:
        print(lose)
        return "Lose, Opponent has Blackjack!!!"
    elif u_score==0:
        print(win)
        return "You won with a blackjack!!!"
    elif u_score>21:
        print(lose)
        return "You went over. You lose!!!"
    elif c_score>21:
        print(win)
        return "Opponent went over. You win!!!"
    elif u_score > c_score:
        print(win)
        return "You win!!!"
    else:
        print(lose)
        return "You lose!!!"
def play_game():
    print(logo)
    user_cards=[]
    computer_cards=[]
    computer_score=-1
    user_score=-1
    is_game_over=False

    for _ in range(2):
        user_cards.append(deal_cards())
        computer_cards.append(deal_cards())
        
    while not is_game_over:

        user_score=calculate_score(user_cards)
        computer_score=calculate_score(computer_cards)

        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")


        if user_score==0 or computer_score==0 or user_score>21:
            is_game_over = True
        else:
            user_should_deal=input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal=='y':
                user_cards.append(deal_cards())
            else:
                is_game_over=True
                
    while computer_score!=0 and computer_score<17:
        computer_cards.append(deal_cards())
        computer_score = calculate_score(computer_cards)
        
    print(f"Your final hand: {user_cards} and final score: {user_score}")
    print(f"Computer final hand: {computer_cards} and final score: {computer_score}")
    print(compare(user_score,computer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")=="y":
    system('cls')
    play_game()
    

    


