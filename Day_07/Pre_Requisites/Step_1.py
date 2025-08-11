#TODO-1: Randomly choose a word from the words_list and assign it to a variable called choose_word and then print it.
import random
words_list=['ant', 'baboon', 'badger', 'bat', 'bear', 'beaver', 'camel', 'cat', 'clam', 'cobra', 'cougar', 'coyote', 'crow', 'deer', 'dog', 'donkey', 'duck', 'eagle', 'ferret', 'fox', 'frog', 'goat', 'goose', 'hawk', 'lion', 'lizard', 'llama', 'mole', 'monkey', 'moose', 'mouse', 'mule', 'newt', 'otter', 'owl', 'panda', 'parrot', 'pigeon', 'python', 'rabbit', 'ram', 'rat', 'raven', 'rhino', 'salmon', 'seal', 'shark', 'sheep', 'skunk', 'sloth', 'snake', 'spider', 'stork', 'swan', 'tiger', 'toad', 'trout', 'turkey', 'turtle', 'weasel', 'whale', 'wolf', 'wombat', 'zebra']

choosen_word=random.choice(words_list)
print(choosen_word)

#TODO-2: Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
guess=input("Guess a letter: ").lower()


#TODO-3: Check if the letter the user guessed (guess) is one of the letters in the choosen_word.
#Print "Right" if it is, Print "Wrong" if it is not.
for letter in choosen_word:
    if guess == letter:
        print("Right")
    else:
        print("Wrong")
