Hangman Boot Camp Project
What I have learnt during this journey with AI Core training provider

- It has been a massive learning curve
- Discovered how to the following:
- Use Python for data analysis and manipulation
1. lists: create, append, slice, indexing
2. sets: differences between sets and list, and unique properties of a set
3. dictionaries: what are they, usage, extracting info, etc
4. functions: define, call, arguments, return values
5. Loops: (while, if, for) how to use them and syntax.
6. classes and objects: what they are and how to use them.
- While learning classes and objects I've noticed the syntax code is very similiar to that of C# and Java, which is something I be investigating at a later stage.
- I also discovered the use of git hub for version control and sharing best practises with other individuals. Being honest this is something completely new to me.

Hangman project:
-The hangman project consisted of 4 modules, called milestone 2,3,4,5. Which each milestone file esculating in complexity, and then be given the opportunity to mark changes and simplify to make the various lines of code more easy to read and follow.
please note the following was using python version ..... The following code may not run on different versions. Also you be needing to install a version of conda.

The first stage is create a conditon statement to check the prompt is within acceptable parameters
```
python <milestone_2.py>
```
The next stage was to create a condition to check if the sentered character(letter) is in the selected word.
```
python <milestone_3.py>
```
The third stage was to bring all elements together create a class with relevant functions inside
```
python <milstone_4.py>
```
At this stage a readme file is required and also push (the readme.md, and all 3 python file on tp git hub.)

The final part was to copy and paste code into a new file called milestone_5.py and add a play game function.
The main issue I was finding is linking all the functions together  both inside and outside the class. Also some of the operators 
i orignally had set incorrect, which I am no to worried about, as this happens to some more advanced programmers

How to Play the Game
1. Open Python terminal
2. Select the play button
3. The game will ask the player to enter a letter
4. the game will check to see if the entry is valid and reject anything other than a single letter
5. The game then check if the letter is in the word to guess
6. The game is won is all the letters of the word has been guessed
7. The player has 5 attempts to guess the correct letters
8. After 5 attempts of not guessing the correct letters. The Game is lost
