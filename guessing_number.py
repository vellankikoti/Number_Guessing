import random

name = input("What is Your Name?")
print('Hello,' + name + ' I\'m thinking a number between 1 and 100\n Could you Guess it?')

guesses = []

secret_number = random.randint(1,100)
entered_number = int(input("Guess a number between 1-100: "))
guesses.append(entered_number)

while entered_number != secret_number:
    if entered_number > secret_number:
        print("Number is too High!")
    else:
        print("Number is too Low!")
        
    entered_number = int(input("Guess a number between 0-100: "))
    guesses.append(entered_number)

else:
    print("Congrats, You guessed it!")
    print("It took you {} Guesses to find".format(len(guesses)))
    print("The guesses you tried are: ", guesses)
