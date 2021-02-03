from Airbnb import Airbnb
import datetime
from git_pull import pull

# Set date
date = datetime.datetime.now()

# Set grand total cost
cost = 1263
paid = float((146*3)+(165*2))
unpaid = float(cost - paid)

# Set payments
payments = str(5)

# Prompt 1
prompt_one = ("\nPlease type the number that matches the action you'd like to do today: \n(1) See Payment Details\n(2) See Airbnb Costs")

# Airbnb list
airbnbList = ['Pittsburgh', '$0', 'Chicago', '$867', 'Nashville', '$50', 'New Orleans', '$120', 'Panama City', '$50', 'Savannah', '$176']
# Airbnb("Pittsburgh", 0),
#     Airbnb("Chicago", 867),
#     Airbnb("Nashville", 50),
#     Airbnb("New Orleans", 120),
#     Airbnb("Panama City", 50),
#     Airbnb("Savannah", 176)

# airbnb_info = (airbnb[0].location, airbnb[0].cost)

# for item in airbnb:
#     print(airbnb_info, end=" ")

# print("\n")

pull()
print("Everything's up to date!")

# Greeting everytime
greeting = "Hi Christina!!! How are you today?\n"
get_response = input(greeting)

# Prompts
def prompts():
    response = input("Awesome!" + prompt_one + "\n")
    if response == "1":
        print("As of " + date.strftime("%x")+":\nYou have made " + payments + " payments." + "\nYou have paid $" + str(paid) + "\nYou currently owe $" + str(unpaid))
    elif response == "2":
        print('[%s]' % '\n'.join(map(str, airbnbList)))
    else:
        print("Run command again or have a good day!")

print(prompts())
