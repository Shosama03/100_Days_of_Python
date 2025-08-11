
import random
stages=[
    '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''',
    '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''',
    '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''',
    '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''',
    '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''',
    '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''',
    '''
  +---+
  |   |
      |
      |
      |
      |
========='''
]
words_list=['ant', 'baboon', 'badger', 'bat', 'bear', 'beaver', 'camel', 'cat', 'clam', 'cobra', 'cougar', 'coyote', 'crow', 'deer', 'dog', 'donkey', 'duck', 'eagle', 'ferret', 'fox', 'frog', 'goat', 'goose', 'hawk', 'lion', 'lizard', 'llama', 'mole', 'monkey', 'moose', 'mouse', 'mule', 'newt', 'otter', 'owl', 'panda', 'parrot', 'pigeon', 'python', 'rabbit', 'ram', 'rat', 'raven', 'rhino', 'salmon', 'seal', 'shark', 'sheep', 'skunk', 'sloth', 'snake', 'spider', 'stork', 'swan', 'tiger', 'toad', 'trout', 'turkey', 'turtle', 'weasel', 'whale', 'wolf', 'wombat', 'zebra']


# TODO-1: Create a variable called 'lives' to keep track of the number of lives left.
# Set 'lives' to 6.
lives=6


choosen_word=random.choice(words_list)
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
    guess=input("Guess a letter: ").lower()

    display=""


    for letter in choosen_word:
        if guess == letter:
            display+=guess
            correct_letters.append(guess)
        elif letter in correct_letters:
            display+=letter
            
        else:
            display+="_"
          
    print(display)
    
    # TODO-2: If guess is not a letter in choosen_word, then reduce lives by 1.
    # If lives goes down to 0 then the game should end, and it should print "You Lose!!!"    
    
    if guess not in choosen_word:
      lives-=1
      if lives==0:
        game_over=True
        print("You Lose!!!")
      
    
    
    if "_" not in display:
        game_over=True
        print("You Win!!!")
    
    
    # TODO-3: print the ASCII art from 'stages' that corresponds to the current number of lives the user has.
    
    print(stages[lives])