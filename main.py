from requirement import MENU
from requirement import resources

water = 300
milk = 200
coffee = 100


profit = 0

# checking that what user want to drink and receive money


def entered_money():
    global user_choice
    user_choice = input(
        "What would you like? (espresso: 1.5$ /latte: 2.5$ /cappuccino: 3.0$): ").lower()
    if user_choice != "off" and user_choice != "report":
        entered_money = 0
        global money
        money = float(input("please enter the money: "))
    # dollar = int(input("How much 1$ ?"))
    # cents = int(input("How much cents?"))

# report resources


def report():
    global water
    global milk
    global coffee
    global profit
    print(f"Water: {water}ml")
    print(f"Milk: {milk}ml")
    print(f"Coffee: {coffee}gr")
    print(f"profit: {profit}$ ")


# chechking resources and if its enough make the coffe and if its not enough report it


def chek_resources():
    global is_on
    if user_choice == "espresso":
        if water < 50 or coffee < 18:
            print("Sorry we do not have enough resources")
        else:
            make_coffee()
    elif user_choice == "latte":
        if water < 200 or milk < 150 or coffee < 24:
            print("Sorry we do not have enough resources")
        else:
            make_coffee()
    elif user_choice == "cappuccino":
        if water < 250 or milk < 100 or coffee < 24:
            print("Sorry we do not have enough resources")
        else:
            make_coffee()
    elif user_choice == "report":
        report()
    elif user_choice == "off":
        is_on = False
        return is_on

# making the coffe and use resources and add the amount of money to profit


def make_coffee():
    global water
    global milk
    global coffee
    global profit
    if user_choice == "espresso":
        if money == 1.5:
            water -= 50
            coffee -= 18
            profit += 1.5
            print("Here is your espresso☕, enjoy.")
        if money != 1.5:
            print("You insert a wrong amount of money, please try again.")
    elif user_choice == "latte":
        if money == 2.5:
            water -= 200
            milk -= 150
            coffee -= 24
            profit += 2.5
            print("Here is your latte☕, enjoy.")
        if money != 2.5:
            print("You insert a wrong amount of money, please try again.")
    elif user_choice == "cappuccino":
        if money == 3.0:
            water -= 250
            milk -= 100
            coffee -= 24
            profit += 3.0
            print("Here is your cappuccino☕, enjoy.")
        if money != 3.0:
            print("You insert a wrong amount of money, please try again.")
    elif user_choice == "report":
        report()


# for end the while loop
is_on = True
while is_on:

    entered_money()
    chek_resources()
