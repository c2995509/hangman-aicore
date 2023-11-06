#import random

#Create a list of fruits and print
#word_list=('apple', 'orange', 'kiwi', 'plum', 'peach')
#print(word_list)
#Using the random method to select word from list
#word = random.choice(word_list)

#print(word)


def guess():    
    guess = input("please enter a letter?")
    if len(guess) == 1:
        if guess.isalpha() == True:
            print('Good guess!')
        else:
            print('Oops! That is not a valid input.')
guess()

