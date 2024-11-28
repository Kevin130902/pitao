# Exercício: Sistema de Mercado Simples
# Objetivo: Criar um sistema de mercado que permita ao usuário adicionar produtos ao carrinho, visualizar o carrinho, calcular o total e finalizar a compra.

from datetime import datetime
import time

cmds = ["add", "remove", "cart", "clear", "calc", "wallet", "buy", "exit"]

products = {
    "drill": 55.00,
    "hat": 45.03,
    "cola": 5.30,
    "milk": 8.50,
    "rice": 40.99,
    "meat": 30.99,
    "fish": 22.00,
}

class Product:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

cart: list[Product] = []
money = 300.00

def formatCurrency(n: float):
    return f"R${n:1.2f}"

def formatItemAmountMessage(amount: int):
    return f"time{'s' if amount != 1 else ''}"

def getTotalPrice() -> float:
    total = 0

    for item in cart:
        total += item.price

    return total

def getItemCount():
    viewedItems: dict[str, int] = {}

    for item in cart:
        if item.name in viewedItems:
            viewedItems[item.name] += 1
        else:
            viewedItems[item.name] = 1

    return viewedItems.items()

def printNote(s: str):
    noteName = f"nota-{time.time_ns()}.txt"
    f = open(noteName, "x", encoding="utf8")
    f.write(s)
    f.close()

firstTime = False
while True:
    if not firstTime:
        print("==============================================")
        print("Welcome to my virtual store\n")
        cmdNames = "Commands: "
        ps = "Available Products:"

        for cmd in cmds:
            cmdNames += cmd + " "

        for pName, price in products.items():
            ps += f"\n- Name: {pName.capitalize()}\n  Price: {formatCurrency(price)}"

        print(cmdNames + "\n" + ps)
        print("==============================================")
        
        firstTime = True

    #

    op = input("\nSelect a valid command\n~ ")

    match op:
        case "add":
            itemName = input("\nProvide a product name: ").lower()

            if not itemName in products:
                print("The chosen product doesn't exist.")
                continue

            itemAmount = int(input("Provide the amount of items you wish to add: "))

            if itemAmount < 0:
                print("Invalid amount.")
                continue
                
            if itemName in products:
                for _ in range(itemAmount):
                    cart.append(Product(itemName, products[itemName]))

                print(f"The product '{itemName}' was added {itemAmount} {formatItemAmountMessage(itemAmount)} to the cart.")
            else:
                print(f"The product '{itemName}' was not found. Please provide a valid product name.")

        case "remove":
            itemName = input("\nProvide a product name: ").lower()

            if not itemName in products:
                print("The chosen product doesn't exist.")
                continue

            itemAmount = int(input("Provide the amount of items you wish to remove: "))

            if itemAmount < 0:
                print("Invalid amount.")
                continue

            deletedItems = 0
            i = 0
            for _ in range(len(cart)):
                item = cart[i]
                if item.name == itemName:
                    deletedItems += 1
                    del cart[i]
                else:
                    i += 1

                if deletedItems == itemAmount:
                    break

            if deletedItems >= 0:
                print(f"The product '{itemName}' was removed {deletedItems} {formatItemAmountMessage(deletedItems)} from the cart.")
            else:
                print(f"The product '{itemName}' was not found in the cart.")
        case "cart":
            if len(cart) > 0:
                for itemName, amount in getItemCount():
                    print(f"- {itemName.capitalize()} (x{amount})\n  {formatCurrency(products[itemName] * amount)}")
            else:
                print("The cart is currently empty.")

        case "clear":
            cart.clear()

            print("The cart was successfuly cleared.")
        case "calc":
            print(f"The total price of the purchase is {formatCurrency(getTotalPrice())}")
        case "wallet":
            print(f"Your current credit amount is {formatCurrency(money)}")
        case "buy":
            if len(cart) == 0:
                print("The cart is currently empty.")
                continue

            total = getTotalPrice()
            if money >= total:
                s = f"=================NOTE====================\n{datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n\nPRODUCTS:\n"

                for itemName, amount in getItemCount():
                    s += f"{itemName.upper()} x{amount} - {formatCurrency(products[itemName] * amount)}\n"
        
                s += f"\nTOTAL: {formatCurrency(total)}\n" + "========================================="

                printNote(s)

                cart.clear()
                money -= total

                print(f"The purchase was successfuly finished! your current credit amount is {formatCurrency(money)}")
            else:
                print("Insufficient credits.")
        case "exit":
            break
        case _:
            print("Invalid command.")