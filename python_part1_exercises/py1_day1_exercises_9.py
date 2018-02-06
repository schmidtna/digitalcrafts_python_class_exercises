coin_count = 0
print("You have" + coin_count + "coins.")
if coin_count >= 0:
    stay_go = input("Do you want another coin? yes/no ").lower()
    if stay_go == "yes" or "y":
        print("You now have" (coin_count + 1) "coins.")
else:
    coin_count = -1
    print("Bye")