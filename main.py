import random
import math

lower_bound = int(input("Enter lower bound (smaller number) - ")) 
upper_bound = int(input("Enter upper bound (bigger number) - ")) 

random_num = random.randint(lower_bound, upper_bound)

max_tries = round(math.log(upper_bound-lower_bound+1, 2))

print("You have only ", max_tries , " tries to guess the right number.")

i = 0

while i < max_tries:
    i += 1

    guess = int(input("Enter your guess now!"))

    if (guess == random_num):
        print("Well done you guessed the number in just " , i , " number of tries")
        break
    elif (guess < random_num):
        print("Your guess was lower than the random number!")
    elif (guess > random_num):
        print("Your guess was higher than the random number!")

if i >= max_tries:
    print("The number is " , random_num)
    print("Better luck next time!")