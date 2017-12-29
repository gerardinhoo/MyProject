# !/usr/bin/python

#  These are the three texts I've based my game on. Easy, Medium and hard quiz.
easy = """ France is an western europe country whose capital is __1__. The Frenchmen have
elected a new president in May 2017. His name is __2__. The language spoken in France is__3__.
The French open is also known as __4__."""  # This is the easy level

medium = """The first rule about the Pythonista's guide to all problems is to not __1__.
In python, we use two ways to refer to the same object.\n We call it __2__.  The sequence of characters
surrounded by quotes are called __3__. To remove a file in Python we use__4__.""" # This is the medium level

hard = """ __1__ was the first U.S president to servemore than two terms. The oldest U.S
president elected was __2__. The first president to live in the White House was __3__. The signature
of the purchase of Alaska from Russia was signed by __4__.""" # This is the hard level

#  Here I used the dictionnary to store the data of the game. This data contains the list of the three levels\n(easy,medium,hard )/n. In this data we also have the correct answers of each level.
data = {
    'easy': {
        'phrase': 'Easy __1__  .  __2__ .  __3__  .   __4__ .',
        'answers': ['paris', 'macron', 'french', 'roland garros'],
        'question': """ France is an western europe country whose capital is __1__ .The Frenchmen have elected a new president in May 2017.
                        His name is __2__. The language spoken in France is__3__. The French open is also known as __4__.""" , # This is the easy level text
        'correct_answer1': 'paris', # 
        'answer1': 'Correct! France is an western europe country whose capital is __paris__.',
        'correct_answer2': 'macron',
        'answer2': 'Correct! The Frenchmen have elected a new president in May 2017. His name is __macron__.',
        'correct_answer3': 'french',
        'answer3': 'Correct! The language  spoken in France is __french__.',
        'correct_answer4': 'roland garros',
        'answer4': 'Correct! The French open is also known as __roland garros__.'
        

       
    },
    'medium': {
        'phrase': 'Medium __1__  .  __2__ .  __3__  .   __4__ .',
        'answers': ['panic', 'aliases', 'strings', 'rm'],
        'question': """The first rule about the Pythonista's guide to all problems is to not __1__. In python, we use two ways to refer to the same object.
                       We call it __2__.  The sequence of characters surrounded by quotes are called __3__.
                       To remove a file in Python we use__4__.""" ,# This is the medium level text
        'correct_answer1': 'panic',
        'answer1': '''Correct! The first rule about the Pythonista's guide to all problems is to not __panic__.''',
        'correct_answer2': 'aliases',
        'answer2':'Correct! In python we use two ways to refer to the same object. We call it __aliases__.',
        'correct_answer3': 'strings',
        'answer3':'Correct! The sequence of characters surrounded by quotes are called __strings__.',
        'correct_answer4': 'rm',
        'answer4':'Correct! To remove a file in Python we use __rm__'
        
    },
    'hard': {
        'phrase': 'Hard__1__  .  __2__ .  __3__  .   __4__ .',
        'answers': ['roosevelt', 'trump', 'john adams', 'andrew johnson'],
        'question': """ __1__ was the first U.S president to serve more than two terms. The oldest U.S
                       president elected was __2__. The first president to live in the White House was __3__. The signature
                       of the purchase of Alaska from Russia was signed by __4__.""", # This is the hard level text
        'correct_answer1': 'roosevelt',
        'answer1': 'Correct! __roosevelt__ was the first U.S president to serve more than two terms.',
        'correct_answer2': 'trump',
        'answer2': 'Correct! The oldest U.S president elected was __trump__.',
        'correct_answer3': 'john adams',
        'answer3': 'Correct! The first president to ive in the White House was __john adams__.',
        'correct_answer4': 'andrew johnson',
        'answer4': 'Correct! The signature of the purchase of Alaska from Russia was signed by __andrew johnson__.'
    }
}

#A welcome greeting to the player.
player_name = raw_input("Type in your name!")
print "Welcome to my quiz " + player_name + "!"


#  In this part I defined select_level which  will prompt the players to choose the \n difficulty of the game.( Easy, Medium and Hard).
def select_level(): 
    while True:
        level = raw_input('Choose a difficulty: (easy / medium / hard)\n').lower()
        if level in data:
           return level
        print 'Incorrect level! Try again!'
        
mylevel = select_level()

print data[mylevel]['question']


#  Here the player plays the game by guessing the correct answer to the first question.
def first_answer():
    while True:
         answer = raw_input('What should we substituted for __1__?').lower()
         if answer in data[mylevel]['correct_answer1']:
            print data[mylevel]['answer1']
            return
         else:
             print 'Incorrect! Try again!'
         
first_answer() 


#  Here the player plays the game by guessing the correct answer to the second question.
def second_answer():
    while True:
         answer = raw_input('What should we substituted __2__?').lower()
         if answer in data[mylevel]['correct_answer2']:
             print data[mylevel]['answer2']
             return
         else:
             print 'Incorrect! try again!'

second_answer()


#  Here the player plays the game by guessing the correct answer to the third question.
def third_answer():
    while True:
        answer = raw_input('What should we substituted for __3__?').lower()
        if answer in data[mylevel]['correct_answer3']:
            print data[mylevel]['answer3']
            return
        
        else:
            print 'Incorrect! try again!'
        

third_answer()

#  Here the player plays the game by the correct answer to the fourth question.
def fourth_answer():
    while True:
        answer = raw_input('What shoud we substituted for __4__?').lower()
        if answer in data[mylevel]['correct_answer4']:
            print data[mylevel]['answer4']
            return
        else:
             print 'Incorrect! try again!'
        
fourth_answer()


# Congratulations words to the player for a job well done.

print "Congratulations! You have passed the test!"





        

