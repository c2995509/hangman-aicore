import random
# A list of words
word_list=('apple', 'orange', 'kiwi', 'plum', 'peach')
#Using the inbuilt python function select a word from give list
word = random.choice(word_list)

def ask_for_input():
    while True:   
        guess = input("please enter a letter?")
        guess=guess.lower()
        if len(guess) == 1 and guess.isalpha() == True:
            #print('Good guess!')
            break
        else:
            print('Invalid letter. Please, enter a single alphabetical character.')
    return guess
ask_for_input()


def check_guess():
    guess=ask_for_input()
    while True:
        if guess in word:
            print('Good guess!',guess, 'is in the word')
            break
        else:
            print('Sorry,',guess,' is not in the word. Try again.')
            
    return guess
check_guess()