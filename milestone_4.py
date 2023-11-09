class Hangman:
    def __init__(self,word_list,num_lives=5):
        self.word_list = word_list
        self.word = self.word_select()
        self.list_of_guesses = []
        self.word_guessed =['_']*len(self.word)
        self.num_letters =len(set(self.word))
        self.num_lives = num_lives
        
        
                
    # A list of words
    def word_select(self):
        import random
        word = random.choice(self.word_list)
        return word

    list_of_guesses=[]
   
    def ask_for_input(self):
        #word_selected=word_selected()
        while True:   
            guess = input("please enter a letter?")
            guess=guess.lower() 
            if len(guess) == 1 and guess.isalpha() == True:
                print('Valid input')
                break
            elif guess in enumerate (self.list_of_guesses):
                print("you've already tried that letter!")
            else:
                print('Invalid letter. Please, enter a single alphabetical character.')
                pass
        self.list_of_guesses.append(guess)
        return guess
    #ask_for_input()

    def check_guess(self):
                #word_selected=word_selected()
        while True:
            guess = self.ask_for_input()
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
                self.list_of_guesses.append=guess
                pass
        
    #check_guess(self)

my_word_list=('apple', 'orange', 'kiwi', 'plum', 'peach','pineapple','banana')           
game = Hangman(my_word_list)   

#game.ask_for_input()
game.check_guess()
