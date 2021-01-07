import datetime

# Set date
date = datetime.datetime.now()

# Set grand total cost
cost = 1146
paid = float(146)
unpaid = float(cost - paid)

# Set payments
payments = str(1)

# Greeting everytime
greeting = "Hi Christina! Would you like to see your payment track? (Y/N) "
see_details = input(greeting)

if see_details == 'y' or see_details == 'Y':
    update = "As of " + date.strftime("%x")+":\nYou have made " + payments + " payments." + "\nYou have paid $" + str(paid) + "\nYou currently owe $" + str(unpaid)
    print(update)
elif see_details == 'n' or see_details == 'N':
    print("OK. Have a good day")
else:
    print("Hehe. That's a no-no. You must enter Y or N.")