import random
print('What is Your Name?')
name = input()
secret_number = random.randint(1,50)
print('Hell0,' + name + ' I\'m thinking a number between 1 and 50')
#Ask the Player to guess 5 times
for guesses in range(1,6):
	print('Take a Guess!')
	guess = int(input())
	if guess < secret_number:
		print('Your guess is lower than my number')
	elif guess > secret_number:
		print('Your guess is higher than my number')
	else:
		break
if guess == secret_number:
	print('Good Job!'+ name +'You guessed my number in'+ str(guesses) +' guesses' )
else:
	print('Nope,You failed to guess,my guessed number was' + str(secret_number))