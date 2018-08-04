import random
print('What is Your Name?')
name = input()
secret_number = random.randint(1,100)
print('Hello,' + name + ' I\'m thinking a number between 1 and 100')
guesses = []

secret_number = random.randint(1,100)

player = int(input("Guess a number between 1-100: "))
guesses.append(player)

while player != secret_number:
    if player > secret_number:
        print("Number is too High!")
    else:
        print("Number is too Low!")
    player = int(input("Guess a number between 0-100: "))
    guesses.append(player)

else:
    print("Congrats, You guessed it!")
    print("It took you {} Guesses to find".format(len(guesses)))
    print("The guesses you tried are: ", guesses)
