
import random
words_list=['ant', 'baboon', 'badger', 'bat', 'bear', 'beaver', 'camel', 'cat', 'clam', 'cobra', 'cougar', 'coyote', 'crow', 'deer', 'dog', 'donkey', 'duck', 'eagle', 'ferret', 'fox', 'frog', 'goat', 'goose', 'hawk', 'lion', 'lizard', 'llama', 'mole', 'monkey', 'moose', 'mouse', 'mule', 'newt', 'otter', 'owl', 'panda', 'parrot', 'pigeon', 'python', 'rabbit', 'ram', 'rat', 'raven', 'rhino', 'salmon', 'seal', 'shark', 'sheep', 'skunk', 'sloth', 'snake', 'spider', 'stork', 'swan', 'tiger', 'toad', 'trout', 'turkey', 'turtle', 'weasel', 'whale', 'wolf', 'wombat', 'zebra']

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


# TODO-1: Use a while loop to let the user guess again.
game_over=False
correct_letters=[]
while not game_over:
    guess=input("Guess a letter: ").lower()

    display=""
    # TODO-2: Change the for loop so that you keep the previous correct letters in display.


    for letter in choosen_word:
        if guess == letter:
            display+=guess
            correct_letters.append(guess)
        elif letter in correct_letters:
            display+=letter
            
        else:
            display+="_"
    print(display)
    
    if "_" not in display:
        game_over=True
        print("You Win!!!")
        