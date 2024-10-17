# Exercício: Sistema de Mercado Simples
# Objetivo: Criar um sistema de mercado que permita ao usuário adicionar produtos ao carrinho, visualizar o carrinho, calcular o total e finalizar a compra.

from datetime import datetime
import time

cmds = ["add", "remove", "cart", "clear", "calc", "wallet", "buy"]

products = {
    "furadeira": 55.00,
    "chapéu": 45.03,
    "coca lata": 5.30,
    "cigarro": 3.00,
    "leite": 8.50,
    "arroz": 40.99,
    "carne": 30.99,
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
    return f"vez{'es' if amount != 1 else ''}"

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
        print("Seja bem-vindo a loja virtual do python\n")
        cmdNames = "Comandos: "
        ps = "Produtos Disponíveis:"

        for cmd in cmds:
            cmdNames += cmd + " "

        for pName, price in products.items():
            ps += f"\n- Nome: {pName.capitalize()}\n  Preço: {formatCurrency(price)}"

        print(cmdNames + "\n" + ps)
        print("==============================================")
        
        firstTime = True

    #

    op = input("\nSelecione um comando válido\n~ ")

    match op:
        case "add":
            itemName = input("\nDigite o nome do produto: ").lower()

            if not itemName in products:
                raise ValueError("O produto selecionado não existe.")

            itemAmount = int(input("Digite a quantidade que deseja adicionar: "))

            if itemAmount < 0:
                raise ValueError("Quantidade inválida.")
                
            if itemName in products:
                for _ in range(itemAmount):
                    cart.append(Product(itemName, products[itemName]))

                print(f"Produto '{itemName}' foi adicionado {itemAmount} {formatItemAmountMessage(itemAmount)} ao carrinho.")
            else:
                print(f"O produto '{itemName}' não foi encontrado. Digite um nome de produto válido")

        case "remove":
            itemName = input("\nDigite o nome do produto que deseja remover: ").lower()

            if not itemName in products:
                raise ValueError("O produto selecionado não existe.")

            itemAmount = int(input("Digite a quantidade que deseja remover: "))

            if itemAmount < 0:
                raise ValueError("Quantidade inválida.")

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
                print(f"O produto '{itemName}' foi removido {deletedItems} {formatItemAmountMessage(deletedItems)} do carrinho.")
            else:
                print(f"O produto '{itemName}' não foi encontrado no carrinho.")
        case "cart":
            if len(cart) > 0:
                for itemName, amount in getItemCount():
                    print(f"- {itemName.capitalize()} (x{amount})\n  {formatCurrency(products[itemName] * amount)}")
            else:
                print("O carrinho está vazio.")

        case "clear":
            cart.clear()

            print("O carrinho foi limpo com sucesso.")
        case "calc":
            print(f"O preço total da compra é {formatCurrency(getTotalPrice())}")
        case "wallet":
            print(f"Seu saldo atual é de {formatCurrency(money)}")
        case "buy":
            if len(cart) == 0:
                print("O carrinho está vazio.")
                continue

            total = getTotalPrice()
            if money >= total:
                s = f"===============NOTA FISCAL===============\n{datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n\nPRODUTOS:\n"

                for itemName, amount in getItemCount():
                    s += f"{itemName.upper()} x{amount} - {formatCurrency(products[itemName] * amount)}\n"
        
                s += f"\nTOTAL: {formatCurrency(total)}\n" + "========================================="

                printNote(s)

                cart.clear()
                money -= total

                print(f"Compra efetuada com sucesso! seu saldo atual é de {formatCurrency(money)}")
            else:
                print("Saldo insuficiente.")
        case "exit":
            break
        case _:
            print("Operação inválida.")