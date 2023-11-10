import random
'''
This is a game called Hangman
-----------------------------
A player has 5 lives to guess all the letters in a word
The computer randomly selects a word and displays it with underscores for each letter that hasn't been guessed yet.
the player is asked to input a single letter. The game will reject anything other inputs
The game will then check if the letter is in the word, if not the player loses a life, if correct the letter is shown 
The process is repeated until either the player loses all their lives or has guessed the word

'''

class Hangman:
    def __init__(self,word_list,num_lives=5):
        self.word_list = word_list
        self.word = random.choice(word_list)
        self.list_of_guesses = []
        self.word_guessed =['_']*len(self.word)
        self.num_letters =len(set(self.word))
        self.num_lives = num_lives
        

 
   #Check if input is valid
    def ask_for_input(self):
       #word_selected=word_selected()
        while True:
            
            guess = input("please enter a letter?").lower()
                    
           #Cchecks that a player inputs only a single letter
            if len(guess) == 1 and guess.isalpha() == True:
                print('Valid input')
                #Check if a player has already entered a letter previously
                if guess in self.list_of_guesses:
                    print('You have already entered that letter! Try again.')
                else:
                    break
            else:
                print('Invalid letter. Please, enter a single alphabetical character.')
                pass
        ##Updates the list of letters entered    
        self.list_of_guesses.append(guess)
        self.check_guess(guess)
        

    
    def check_guess(self,guess):
        #Check if guess is in the selected word                
        if guess in self.word:
            print('Good guess!',guess, 'is in the word')
            #player has entered a letter in the word and replaces '_' with guessed letter(s)
            for idx,letter in enumerate(self.word_list):
                if letter==guess:
                    self.word_guessed[idx]=guess
                    
            #Reduces the number of unqiue letters player still needed to guess
            self.num_letters -= 1       
        else:
            #player has entered a letter not in the word list and loses a life
            print('Sorry,',guess,' is not in the word. Try again.')
            self.num_lives -= 1
            print('You have ', self.num_lives , ' lives left')

       




def play_game(word_list):
    num_lives=5
    #create an instance of the class and assigning to the varaiable called game links this method to the class
    game=Hangman(word_list,num_lives)
  
    while True:
        #checks the status of the games by looking into the class
        #Game status no lives, and not all letters guessed then plaer lost
        if game.num_lives == 0 and game.num_letters > 0:
            print("You've lost better luck next time!")
            break
        #Game status has lives but not guessed all the letters, player to guess another letter
        elif game.num_lives > 0 and game.num_letters > 0 :
            game.ask_for_input()
        ##Game Status, player has guessed all letters of the word and won    
        elif game.num_lives > 0 and game.num_letters == 0:
            print('Congratulations.You won the game!')
            break

play_game(['apple', 'orange', 'kiwi', 'plum', 'peach','pineapple','banana'])