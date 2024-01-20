import random


random_number = random.randint(1, 10)

while True:

    user_guess = int(input("Guess the number between 1 and 10: "))


    if user_guess == random_number:
        print("Bravo!, You guessed the number.")
        break
    elif user_guess < random_number:
        print("Too low. Try again.")
    else:
        print("Too high. Try again.")
