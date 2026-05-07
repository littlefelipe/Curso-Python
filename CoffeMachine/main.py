from data import MENU
from data import resources
import sys

def process_coins(coffee_type):
    """Processa o recebimento das moedas, decidindo o troco e retornando o dinheiro recebido"""
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    received_money = 0
    total_input = (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)
    if total_input < MENU[coffee_type]['cost']:
        print("Sorry that's not enough money. Money refunded.")
    else:
        received_money = MENU[coffee_type]['cost']
        change = total_input - received_money
        print(f"Here is ${change:.2f} in change.")
        print(f"Here is your {coffee_type}. Enjoy")
        return received_money
    return received_money

def make_coffee(coffee_type):
    """Checa se a máquina tem os ingredientes necessários para produzir a bebida desejada.
    Se sim, a bebida é feita e o dinheiro recebido é retornado"""
    water = MENU[coffee_type]['ingredients']['water']
    try:
        milk = MENU[coffee_type]['ingredients']['milk']
    except KeyError:
        milk = 0
    coffee = MENU[coffee_type]['ingredients']['coffee']
    received_money = 0
    if water > resources['water'] or milk > resources['milk'] or coffee > resources['coffee']:
        print("Sorry there is not enough resources")
    else:
        received_money = process_coins(coffee_type)
        resources['water'] -= water
        resources['milk'] -= milk
        resources['coffee'] -= coffee
    return received_money

def console(total_money):
    """Lida com a entrada inicial do console e retorna o valor atualizado do total de dinheiro"""
    coffee_type = input("What would you like? (espresso/latte/cappuccino): ")
    if coffee_type == 'off':
        sys.exit(0)
    elif coffee_type == 'report':
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money ${total_money}")
    elif coffee_type == 'espresso' or coffee_type == 'latte' or coffee_type == 'cappuccino' or coffee_type == 'report':
        total_money += make_coffee(coffee_type)
    return total_money

money = 0
while True:
    money = console(money)