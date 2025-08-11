
import random

from Hangman_words import word_list
from Hangman_art import stages,logo

lives=6

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
    
    print(f"****************************{lives}/6 LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()
    
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
    
    
    if guess not in choosen_word:
      lives-=1
      print(f"You guessed {guess}, that's not in the word. You lose a life.")
      if lives==0:
        game_over=True
        print(f"*********************IT WAS {choosen_word}! YOU LOSE***************************")
      

    if "_" not in display:
        game_over=True
        print("***********************YOU WIN!!!***************************")
    
     
    print(stages[lives])