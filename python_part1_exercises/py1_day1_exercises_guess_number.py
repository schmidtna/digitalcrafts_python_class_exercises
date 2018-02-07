import random
secret_number = random.randint(1, 10)
chances = 5

while True:
    print("I am thinking of a number between 1 and 10")
    print("You have " + str(chances) + " guesses left.")
    player_guess = int(input("Try and guess the number! "))
    if player_guess > secret_number:
        print("Your guess was too high, try again!")
        chances -= 1
    elif player_guess < secret_number:
        print("Your guess was too low, try again!")
        chances -= 1
    elif player_guess == secret_number:
        print("Congrats! You guessed the number!")
        replay = input("Would you like to play again? ").lower
        if replay == "yes" or "y":
            secret_number = random.randint(1, 10)
            chances = 5
        else:
            chances = -1 
            print("Thanks for playing!")
            break
    if chances < 1:
        print("Sorry, you ran out of chances.")
        replay = input("Would you like to play again? ").lower
        if replay == "yes" or "y":
            secret_number = random.randint(1, 10)
            chances = 5
        else:
            chances = -1
            print("Thanks for playing!")
            break

