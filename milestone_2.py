import random
# A list of words
word_list=('apple', 'orange', 'kiwi', 'plum', 'peach')
#Using the inbuilt python function select a word from give list
word = random.choice(word_list)
print(word)
#Check if user input is valid
while True:   
    #Prompt user for an input
    guess = input("please enter a letter?")
    #If statement to confirm input is  a single character and also a letter
    if len(guess) == 1 and guess.isalpha() == True:
        #print('Good guess!')
        break
    else:
        print('Invalid letter. Please, enter a single alphabetical character.')


#Check to see if the letter selected is in the random word selected
while True:
    if guess in word:
        print('Good guess!',guess, 'is in the word')
        break
    else:
        print('Sorry,',guess,' is not in the word. Try again.')
        pass





