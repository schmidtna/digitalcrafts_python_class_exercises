bill_total = float(input("Total bill amount? "))
good = bill_total * .20
fair = bill_total  * .15
bad = bill_total * .10
service_quality = input("How was the service? Good, fair, or bad: ").lower()

if service_quality == "good":
    print("Tip amount: $""{:.2f}".format(good))
    print("Total bill: $""{:.2f}".format(bill_total + good))
elif service_quality == "fair":
    print("Tip amount: $""{:.2f}".format(fair))
    print("Total bill: $""{:.2f}".format(bill_total + fair))
else:
    print("Tip amount: $""{:.2f}".format(bad))
    print("Total bill: $""{:.2f}".format(bill_total + bad))
