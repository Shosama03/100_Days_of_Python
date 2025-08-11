
import random
words_list=['ant', 'baboon', 'badger', 'bat', 'bear', 'beaver', 'camel', 'cat', 'clam', 'cobra', 'cougar', 'coyote', 'crow', 'deer', 'dog', 'donkey', 'duck', 'eagle', 'ferret', 'fox', 'frog', 'goat', 'goose', 'hawk', 'lion', 'lizard', 'llama', 'mole', 'monkey', 'moose', 'mouse', 'mule', 'newt', 'otter', 'owl', 'panda', 'parrot', 'pigeon', 'python', 'rabbit', 'ram', 'rat', 'raven', 'rhino', 'salmon', 'seal', 'shark', 'sheep', 'skunk', 'sloth', 'snake', 'spider', 'stork', 'swan', 'tiger', 'toad', 'trout', 'turkey', 'turtle', 'weasel', 'whale', 'wolf', 'wombat', 'zebra']

choosen_word=random.choice(words_list)
print(choosen_word)

# TODO-1: Create a "placeholder" with the same number of blanks as the choosen_word
#Dr.Angela Yu's Method
'''
    placeholder=""
    word_length=len(choosen_word)
    for position in range(word_length):
        placeholder+="_"
    print(placeholder)
'''
#My Own Method :)
print('_'*len(choosen_word))
guess=input("Guess a letter: ").lower()

# TODO-2: Create a "Display" that puts the guess letter in the right place in the "placeholder"

display=""
for letter in choosen_word:
    if guess == letter:
        display+=guess
    else:
        display+="_"
print(display)