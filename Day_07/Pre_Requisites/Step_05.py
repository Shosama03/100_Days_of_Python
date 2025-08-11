
import random


# TODO-1:  Update the word_list to use the 'word_list' from hangman_words.py
from Hangman_words import word_list
from Hangman_art import stages,logo


lives=6


# TODO-3: Import the logo from hangman_art.py and print it at the start of the game.
print(logo)

choosen_word=random.choice(word_list)
print(choosen_word)

#Dr.Angela Yu's Method

placeholder=""
word_length=len(choosen_word)
for position in range(word_length):
    placeholder+="_"
print(placeholder)

#My Own Method :)
#print('_'*len(choosen_word))



game_over=False
correct_letters=[]
while not game_over:
    
    # TODO-6: Update the code below to tell the user how many lives they have left.
    print(f"****************************{lives}/6 LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()
    
    # TODO-4: If the user enters a letter they've already guessed, print the letter and let them know.
    if guess in correct_letters:
        print(f"You've already guessed {guess}") 

    display=""


    for letter in choosen_word:
        if guess == letter:
            display+=guess
            correct_letters.append(guess)
        elif letter in correct_letters:
            display+=letter
            
        else:
            display+="_"
          
    print("Word to guess: "+ display)
    
    # TODO-5: If the letter is not in the choosen_word, print out the letter and let them know it's not in the word.
    
    
    
    
    if guess not in choosen_word:
      lives-=1
      print(f"You guessed {guess}, that's not in the word. You lose a life.")
      if lives==0:
        game_over=True
        
        
        # TODO-7: Update the print statement below to give the user the correct word after losing.
        print(f"*********************IT WAS {choosen_word}! YOU LOSE***************************")
      
    
    
    if "_" not in display:
        game_over=True
        print("***********************YOU WIN!!!***************************")
    
    
    
    # TODO-2: Update the code below to use the stages list from the file 'hangman_art.py' 
    print(stages[lives])