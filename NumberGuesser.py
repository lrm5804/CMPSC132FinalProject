# CMPSC 132 FINAL PROJECT
# Linnea Miller
# NumberGuesser

class NumberGuesser:

    def __init__(self) -> None:
        pass

    def play(self):
        break_line = '---------------------------------------------------------------------------------------------------------------------------------------------------------------------------'

        print('WELCOME TO GUESS THE NUMBER!\n')

        answer1 = input("Have you played before? Type Y or N: ")
        
        if answer1 in 'Nn':
            print("\nHere are the directions:")
            print("I will think of a number in a given range. Your job is to guess the number. I'll give you feedback, and you can keep guessing!")
        else:
            print('\nOk, we can skip the directions!')

        print(break_line)
        print('\nFirst, pick a level.')