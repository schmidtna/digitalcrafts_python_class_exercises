coin_count = 0
answer = " "
print("You have " + str(coin_count) + "coins.")
while answer != "no":
    answer = input("Would you like another coin? ")
    if answer.lower == "yes" or "y":
        coin_count = coin_count + 1
        print("You now have " + str(coin_count) + "coins.")
print("bye")
    