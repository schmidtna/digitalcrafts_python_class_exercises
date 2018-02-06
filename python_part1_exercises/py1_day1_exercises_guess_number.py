secret_number = 5
print("I am thinking of a number between 1 and 10")
player_guess = int(input("Try and guess the number! "))
while True:
    if player_guess < secret_number:
        print("Too low, try again!")
        player_guess = int(input("Guess what the number is "))
    elif player_guess > secret_number:
        print("Too high, try again!")
        player_guess = int(input("Guess what the number is "))
    else:
        print("Congrats! You got it!")
        break