# importing the modules required for this game which are the random module to guess the number and the math module to calculate the number of guesses given for the player.
import random
import math

# storing the upper bound and lower bound in variables in order to use it later to generate the number
lower_bound = int(input("Enter lower bound (smaller number) - ")) 
upper_bound = int(input("Enter upper bound (bigger number) - ")) 

# using the bounds to generate a random number 
random_num = random.randint(lower_bound, upper_bound)

# calculating the number of guesses according to the given bounds
max_tries = round(math.log(upper_bound-lower_bound+1, 2))

# Letting the user know how many tries that they have
print("You have only ", max_tries , " tries to guess the right number.")

i = 0

# Using a while loop to check evrything
while i < max_tries:
    i += 1

    guess = int(input("Enter your guess now!"))

    if (guess == random_num):
        if (i == 1):
            print ("Well done you guessed the number in just" , i , "try")
        else:
            print("Well done you guessed it with" , i , "tries")
        break
    elif (guess < random_num):
        print("Your guess was lower than the random number!")
    elif (guess > random_num):
        print("Your guess was higher than the random number!")

    if i >= max_tries:
        print("The number is " , random_num)
        print("Better luck next time!")