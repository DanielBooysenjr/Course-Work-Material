
# Coffee Machine Program

from menu import MENU, resources

off = False

total_money_inserted = 0
money_in_machine = 0


def insert_coins(total_money_inserted):
    
    global money_in_machine

    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    quarters = 0.25 * quarters

    dimes = int(input("How many dimes?: "))
    dimes = 0.1 * dimes

    nickles = int(input("How many nickles?: "))
    nickles = 0.05 * nickles

    pennies = int(input("How many pennies?: "))
    pennies = 0.01 * pennies

    total_money_inserted = quarters + dimes + nickles + pennies
    money_in_machine += total_money_inserted

    return total_money_inserted


def espresso(total_money_inserted):
    if total_money_inserted == 1.5:
        print("Here is your espresso ☕")
    elif total_money_inserted > 1.5:
        change_due(total_money_inserted)
    resources["water"] -= 50
    resources["coffee"] -= 18
    if total_money_inserted < 1.5:
        return print("You don't have enough money. Here is your money back.")


def latte(total_money_inserted):
    if total_money_inserted == 2.5:
        print("Here is your latte ☕")
    elif total_money_inserted > 2.5:
        change_due(total_money_inserted)
    resources["water"] -= 200
    resources["milk"] -= 150
    resources["coffee"] -= 24
    if total_money_inserted < 2.5:
        return print("You don't have enough money. Here is your money back.")


def cappuccino(total_money_inserted):

    if total_money_inserted == 3.0:
        print("Here is your cappuccino ☕")
    elif total_money_inserted > 3.0:
        change_due(total_money_inserted)
    else:
        return print("You don't have enough money. Here is your money back.")
    resources["water"] -= 250
    resources["milk"] -= 100
    resources["coffee"] -= 24
    if total_money_inserted < 3.0:
        return print("You don't have enough money. Here is your money back.")


def check_resources(total_money_inserted):
    
    if order == 'espresso':
        if resources["water"] >= 50 and resources["coffee"] >= 18:
            total_money_inserted = insert_coins(total_money_inserted)
            espresso(total_money_inserted)
        else:
            return print("Not enough ingredients")
    elif order == 'latte':
        if resources["water"] >= 200 and resources["milk"] >= 150 and resources["coffee"] >= 24:
            total_money_inserted = insert_coins(total_money_inserted)
            latte(total_money_inserted)
        else:
            return print("Not enough ingredients")
    elif order == "cappuccino":
        if resources["water"] >= 250 and resources["milk"] >= 100 and resources["coffee"] >= 24:
            total_money_inserted = insert_coins(total_money_inserted)
            cappuccino(total_money_inserted)
        else:
            return print("Not enough ingredients")
    else:
        return "Invalid selection. Try again."


def change_due(total_money_inserted):
    
    espresso = 1.5
    latte = 2.5
    cappuccino = 3.0

    if order == 'espresso':
        change = total_money_inserted - espresso
        money_in_machine - change
        print(f"You inserted to much money, here is your espresso ☕ and your change ${change:.2f}")
    elif order == "latte":
        change = total_money_inserted - latte
        money_in_machine - change
        print(f"You inserted to much money, here is your latte ☕ and your change ${change:.2f}")
    elif order == "cappuccino":
        change = total_money_inserted - cappuccino
        money_in_machine - change
        print(f"You inserted to much money, here is your cappuccino ☕ and your change ${change:.2f}")


while not off == True:
        
    order = input("What would you like? (espresso/latte/cappuccino): ").lower()

    money_in_machine +=total_money_inserted    
    if order == "espresso":
        check_resources(total_money_inserted)
    elif order == "latte":
        check_resources( total_money_inserted)
    elif order == "cappuccino":
        check_resources(total_money_inserted)
    elif order == "off":
        print("Thank you for using the coffee machine. Goodbye!")
        off = True
    elif order == "report":
        print("Water:", resources["water"], "ml")
        print("Milk:", resources["milk"], "ml")
        print("Coffee:", resources["coffee"], "g")
        print(f"Money: ${money_in_machine:.2f}")