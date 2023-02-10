
# Coffee Machine Program

from menu import MENU, resources

off = False

quarters_total = 0
dimes_total = 0
nickles_total = 0
pennies_total = 0
total_money_inserted = 0
money_in_machine = 0



def insert_coins(total_money_inserted):
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    quarters = 0.25 * quarters

    print(quarters)
    dimes = int(input("How many dimes?: "))
    dimes = 0.1 * dimes

    print(dimes)
    nickles = int(input("How many nickles?: "))
    nickles = 0.05 * nickles

    print(nickles)
    pennies = int(input("How many pennies?: "))
    pennies = 0.01 * pennies

    print(pennies)
    total_money_inserted = quarters + dimes + nickles + pennies
    print(total_money_inserted)

    return total_money_inserted


def espresso(total_money_inserted):
    if order == "espresso":
        if resources["water"] > 50:
            if total_money_inserted == 1.5:
                print("Here is your espresso")
            elif total_money_inserted > 1.5:
                print("Too much money. Here is your espresso")
            else:
                return print("You don't have enough money. Here is your money back.")
            resources["water"] -= 50
        else:
            return print("Not enough water.")
        if resources["coffee"] > 18:
            resources["coffee"] -= 18
        else:
            return print("Not enough coffee.")


def latte():
    if order == "latte":
        if resources["water"] > 200:
            resources["water"] -= 200
        else:
            return print("Not enough water.")
        if resources["milk"] > 150:
            resources["milk"] -= 150
        else:
            return print("Not enough milk.")
        if resources["coffee"] > 24:
            resources["coffee"] -= 24
        else:
            return print("Not enough coffee.")


def cappuccino():
    if order == "cappuccino":
        if resources["water"] > 250:
            resources["water"] -= 250
        else:
            return print("Not enough water.")
        if resources["milk"] > 100:
            resources["milk"] -= 100
        else:
            return print("Not enough milk.")
        if resources["coffee"] > 24:
            resources["coffee"] -= 24
        else:
            return print("Not enough coffee.")



    


def change():
    pass


while not off == True:

    # 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
    order = input("What would you like? (espresso/latte/cappuccino): ").lower()
        # a. Check the user’s input to decide what to do next.

    if order == "espresso":
        total_money = insert_coins(total_money_inserted)
        money_in_machine += total_money_inserted
        espresso(total_money)
        print(resources)
    if order == "latte":
        total_money = insert_coins(total_money_inserted)
        latte()
        print(resources)
    if order == "cappuccino":
        total_money = insert_coins(total_money_inserted)
        cappuccino()
        print(resources)
        # b. The prompt should show every time action has completed, e.g. once the drink is
        # dispensed. The prompt should show again to serve the next customer.


    # 2. Turn off the Coffee Machine by entering “off” to the prompt.
        # return
        # a. For maintainers of the coffee machine, they can use “off” as the secret word to turn off
        # the machine. Your code should end execution when this happens.
    if order == "off":
        print("Thank you for using the coffee machine. Goodbye!")
        off = True



    # 3. Print report.
        # a. When the user enters “report” to the prompt, a report should be generated that shows
        # the current resource values. e.g.
    if order == "report":
        print(resources["water"])
        print(resources["milk"])
        print(resources["coffee"])
        print(money_in_machine)
        # Water: 100ml
        # Milk: 50ml
        # Coffee: 76g
        # Money: $2.5


    # 4. Check resources sufficient?
        # a. When the user chooses a drink, the program should check if there are enough
        # resources to make that drink.
        # b. E.g. if Latte requires 200ml water but there is only 100ml left in the machine. It should
        # not continue to make the drink but print: “Sorry there is not enough water.”
        # c. The same should happen if another resource is depleted, e.g. milk or coffee.


    # 5. Process coins.
        # a. If there are sufficient resources to make the drink selected, then the program should
        # prompt the user to insert coins.
        # b. Remember that quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
        # c. Calculate the monetary value of the coins inserted. E.g. 1 quarter, 2 dimes, 1 nickel, 2
        # pennies = 0.25 + 0.1 x 2 + 0.05 + 0.01 x 2 = $0.52


    # 6. Check transaction successful?
        # a. Check that the user has inserted enough money to purchase the drink they selected.
        # E.g Latte cost $2.50, but they only inserted $0.52 then after counting the coins the
        # program should say “Sorry that's not enough money. Money refunded.”.
        # b. But if the user has inserted enough money, then the cost of the drink gets added to the
        # machine as the profit and this will be reflected the next time “report” is triggered. E.g.
        # Water: 100ml
        # Milk: 50ml
        # Coffee: 76g
        # Money: $2.5
        # c. If the user has inserted too much money, the machine should offer change.
        # E.g. “Here is $2.45 dollars in change.” The change should be rounded to 2 decimal
        # places.


    # 7. Make Coffee.
        # a. If the transaction is successful and there are enough resources to make the drink the
        # user selected, then the ingredients to make the drink should be deducted from the
        # coffee machine resources.
        # E.g. report before purchasing latte:
        # Water: 300ml
        # Milk: 200ml
        # Coffee: 100g
        # Money: $0
        # Report after purchasing latte:
        # Water: 100ml
        # Milk: 50ml
        # Coffee: 76g
        # Money: $2.5
        # b. Once all resources have been deducted, tell the user “Here is your latte. Enjoy!”. If
        # latte was their choice of drink