bill_total = float(input("Total bill amount? "))
good = bill_total * .20
fair = bill_total  * .15
bad = bill_total * .10
service_quality = input("How was the service? Good, fair, or bad: ").lower()
splitup = float(input("Split the bill how many ways? "))

if service_quality == "good":
    print("Tip amount: $""{:.2f}".format(good))
    print("Total bill: $""{:.2f}".format(bill_total + good))
    print("The amount per person is: $""{:.2f}".format((bill_total + good) / splitup))
elif service_quality == "fair":
    print("Tip amount: $""{:.2f}".format(fair))
    print("Total bill: $""{:.2f}".format(bill_total + fair))
    print("The amount per person is: $""{:.2f}".format((bill_total + fair) / splitup))
else:
    print("Tip amount: $""{:.2f}".format(bad))
    print("Total bill: $""{:.2f}".format(bill_total + bad))
    print("The amount per person is: $""{:.2f}".format((bill_total + bad) / splitup))