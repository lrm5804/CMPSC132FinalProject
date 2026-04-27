# CMPSC 132 FINAL PROJECT
# Linnea Miller
# NumberGuesser


import random

class NumberGuesser:
    
    def __init__(self) -> None:
        self.number = random.randint(0, 100)
        self.level = None
        self.attempts = 0
        self.breakline = '\n---------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n'

    def begin(self):

        print('WELCOME TO GUESS THE NUMBER!\n')

        answer1 = input("Do you want to hear the directions? Type Y or N: ").lower()
        
        if answer1 == 'n':
            print("\nHere are the directions:")
            print("I will think of a number in a given range. Your job is to guess the number. I'll give you feedback, and you can keep guessing!")
        else:
            print('\nOk, we can skip the directions!')

        print(self.breakline)
        print('First, pick a level.')
        answer2 = input("Type E, M, or H for Easy, Medium, or Hard: ").lower()

        if answer2 == 'e':
            self.level = 'Easy'
            print("Let's begin our game at level Easy!")
        elif answer2 == 'm':
            self.level = 'Medium'
            print("Let's begin our game at level Medium!")
        elif answer2 == 'h':
            self.level = 'Hard'
            print("Let's begin our game at level Hard!")

        print(self.breakline)
        answer3 = input("Type start when you're ready to begin the game: ").lower()
     
        if answer3 == 'start':
            self.play()

    def play(self):
        guess = int(input('Take a guess of what number I am thinking of... : '))
        self.attempts += 1

        if self.level == 'Easy':
            print(f'You get 20 guesses in total, so you have {20 - self.attempts} left.')
            if guess == self.number:
                self.win()
            else:
                while guess != self.number and self.attempts < 20:
                    if guess < self.number:
                        print('Guess too low!')
                    else:
                        print('Guess too high!')
                    print(self.breakline)
                    self.play()

        elif self.level == 'Medium':
            print(f'You get 10 guesses in total, so you have {10 - self.attempts} left.')
            if guess == self.number:
                self.win()
            else:
                while guess != self.number and self.attempts < 10:
                    if guess < self.number:
                        print('Guess too low!')
                    else:
                        print('Guess too high!')
                    print(self.breakline)
                    self.play()

        elif self.level == 'Hard':
            print(f'You get 5 guesses in total, so you have {5 - self.attempts} left.')
            if guess == self.number:
                self.win()
            else:
                while guess != self.number and self.attempts < 5:
                    if guess < self.number:
                        print('Guess too low!')
                    else:
                        print('Guess too high!')
                    print(self.breakline)
                    self.play()

        print(self.breakline)

        self.lose()



    def win(self):
        print(f'CONGRATULATIONS! YOU WON! THE NUMBER WAS {self.number} :) ')
        print(self.breakline)
        play_again = input('Would you like to play again? To continue your winning streak, type Y: ').lower()
        if play_again == 'y':
            self.attempts = 0
            self.number = random.randint(0, 100)
            self.begin()
        else:
            print('GAME OVER')

    def lose(self):
        print(f'TRY AGAIN NEXT TIME. YOU LOST. THE NUMBER WAS {self.number} :( ')
        print(self.breakline)
        play_again = input('Would you like to play again? To redeem yourself, type Y: ').lower()
        if play_again == 'y':
            self.attempts = 0
            self.number = random.randint(0, 100)
            self.begin()
        else:
            print('GAME OVER')

        

