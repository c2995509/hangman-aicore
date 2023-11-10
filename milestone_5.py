class Hangman:
    def __init__(self,choose,word_list,num_lives=5):
        self.word_list = word_list
        self.word = self.word_select()
        self.list_of_guesses = []
        self.word_guessed =['_']*len(self.word)
        self.num_letters =len(set(self.word))
        self.num_lives = num_lives
        self.choose = ''
        self.play_cont = ''
        
    def play_hangman(self):
        choose=input('Would you like to play Hangman? y or n').lower()
        if choose == 'y':
            print("Let's play Hangman")
            game.check_guess()
        elif choose == 'n':
            print('Please come again')
        else:
            print('Invalid input! Please enter y or n')
            
    def play_game(self):
        while True:
            if self.num_lives == 0 and self.num_letters >= 0:
                print("You've lost,better luck next time!")
                break
            elif self.num_lives >= 0 and self.num_letters >= 0:
                game.play_continue()
            elif self.num_lives >= 0 and self.num_letters == 0:
                print('Congratulations. You won the game!')
                break

    def play_continue(self):
        play_cont = input('Would you like to continue? y or n').lower()
        if play_cont == 'y':
            game.check_guess()
        elif play_cont == 'n':
            print('Please come again')
        else:
            print('Invalid input! Please enter y or n')
            pass

    def word_select(self):
        import random
    # A list of words
    def word_select(self):
        import random
        word = random.choice(self.word_list)
        return word

    list_of_guesses=[]
   #Check if input is validh
    def ask_for_input(self):
        #word_selected=word_selected()
        while True:   
            guess = input("please enter a letter?").lower()
            #force the input character letter to be in lower case i.e. A to a
            #guess=guess.lower() 
            #if statement to check input is a single character and is a letter using isaplha inbuilt function
            #If input function is a letter and a single charater then proceed
            if len(guess) == 1 and guess.isalpha() == True:
                print('Valid input')
                break
            else:
                print('Invalid letter. Please, enter a single alphabetical character.')
                pass
        #Update the list of letters entered
        self.list_of_guesses.append(guess)
        return guess
    #check for duplicates
    def check_duplicates(self):
        guess = self.ask_for_input()
        for idx,letter in enumerate(self.list_of_guesses):
            if letter == guess:
                print('You have already used this letter! Try again.')
                pass
            else:
                break
        return guess  
    #Check if guess is in the selected word
    def check_guess(self):
                #word_selected=word_selected()
        while True:
            guess = self.check_duplicates()
            if guess in self.word:
                print('Good guess!',guess, 'is in the word')
                for idx,letter in enumerate(self.word_list):
                    if letter==guess:
                        self.word_guessed[idx]=guess
                    else:
                        pass
            else:
                print('Sorry,',guess,' is not in the word. Try again.')
                self.num_lives -= 1
                print('You have ', self.num_lives , ' lives left')
                self.list_of_guesses.append(guess)
                pass


my_word_list=('apple', 'orange', 'kiwi', 'plum', 'peach','pineapple','banana')           
game = Hangman(my_word_list)   

#game.ask_for_input()

game.play_hangman()