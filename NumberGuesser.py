# CMPSC 132 FINAL PROJECT
# Linnea Miller
# NumberGuesser


import random

class NumberGuesser:
    
    def __init__(self) -> None:
        self.number = random.randint(0, 100)
        self.level = None
        self.attempts = 0
        self.wins = 0
        self.guesses = []
        self.breakline = '\n---------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n'

    def begin(self):

        print('WELCOME TO GUESS THE NUMBER!\n')

        answer1 = input("Do you want to hear the directions? Type Y or N: ")
        answer1 = self.validateYN(answer1)
        while not isinstance(answer1, str) or isinstance(answer1, bool):
                print('Enter a valid string.')
                answer1 = input("Do you want to hear the directions? Type Y or N: ")
                answer1 = self.validateYN(answer1)

        if answer1 == 'y':
            print("\nHere are the directions:")
            print("I will think of a number in a given range. Your job is to guess the number. I'll give you feedback, and you can keep guessing!")
        else:
            print('\nOk, we can skip the directions!')

        print(self.breakline)
        print('First, pick a level.')

        answer2 = input("Type E, M, or H for Easy, Medium, or Hard: ")
        answer2 = self.validateLevel(answer2)
        while not isinstance(answer2, str) or isinstance(answer2, bool):
            print('Enter a valid level: E, M, or H.')
            answer2 = input("Type E, M, or H for Easy, Medium, or Hard: ")
            answer2 = self.validateLevel(answer2)

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

        self.play()

    def play(self):

        guess = input('Take a guess of what number I am thinking of... : ')
        guess = self.validateInt(guess)

        while not isinstance(guess, int) or isinstance(guess, bool):
            print('Enter a valid int')
            guess = input('Take a guess of what number I am thinking of... : ')
            guess = self.validateInt(guess)
        
        self.guesses.append(guess)
        
        print(f'Your guesses are: {self.guesses}')
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
        self.wins += 1
        print(f'CONGRATULATIONS! YOU WON! THE NUMBER WAS {self.number} :) ')
        print(f'You have won {self.wins} times this game!')
        print(self.breakline)


        play_again = input('Would you like to play again? To continue your winning streak, type Y or N: ')
        play_again = self.validateYN(play_again)
        while not isinstance(play_again, str) or isinstance(play_again, bool):
            print("Type Y to play again")
            play_again = input('Would you like to play again? To continue your winning streak, type Y or N: ')
            play_again = self.validateYN(play_again)

        if play_again == 'y':
            self.attempts = 0
            self.number = random.randint(0, 100)
            self.begin()
        else:
            print('GAME OVER')

    def lose(self):
        print(f'TRY AGAIN NEXT TIME. YOU LOST. THE NUMBER WAS {self.number} :( ')
        print(self.breakline)
        play_again = input('Would you like to play again? To redeem yourself, type Y or N: ')
        play_again = self.validateYN(play_again)

        while not isinstance(play_again, str) or isinstance(play_again, bool):
            print("Type Y to play again")
            play_again = input('Would you like to play again? To continue your winning streak, type Y or N: ')
            play_again = self.validateYN(play_again)

        if play_again == 'y':
            self.attempts = 0
            self.number = random.randint(0, 100)
            self.begin()
        else:
            print('\nGAME OVER!!')

    def validateYN(self, txt):
        if isinstance(txt, str) and txt in 'YyNn':
            return txt.lower()
        else:
            return False    

    def validateInt(self, num):
        try:
            return int(num)
        except Exception:
            return False
        
    def validateLevel(self, txt):
        if txt in 'EeMmHh':
            return txt.lower()
        else:
            return False


