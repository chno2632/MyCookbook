#from random import random
import random
#from random import randint

print("Welcome to the guessing game")
# Computer guesses a random number between 1 and 10
number_of_guesses: int = 3
user_won = False

# Computer picks a random number between 1 and 10
correct_answer = random.randint(1, 10)

while number_of_guesses > 0:
    user_guess = input("Guess my number: ")
    user_guess = int(user_guess)

    if user_guess == correct_answer:
        print("Good guess")
        print("You are correct")
        user_won = True
        break
    elif user_guess > correct_answer:
        print("Your guess is too high")
    elif user_guess < correct_answer:
        print("Your guess is too low")

    number_of_guesses -= 1
if user_won == True:
    print("You win!")
else:
    print("You lost!")
    print("Correct answer is " + str(correct_answer))
# User guesses the number
# Computer tells user whhetherguess is too low or too high
# User has three guesses before losing the game
