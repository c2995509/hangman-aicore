def ask_for_input():
    while True:   
        guess = input("please enter a letter?")
        if len(guess) == 1 and guess.isalpha() == True:
            #print('Good guess!')
            break
        else:
            print('Invalid letter. Please, enter a single alphabetical character.')
ask_for_input()


def check_guess():
    guess=guess.lower()
    if guess in word:
        print('Good guess!',guess, 'is in the word')
    else:
        print('Sorry,',guess,' is not in the word. Try again.')
check_guess()