# Exercício: Sistema de Mercado Simples
# Objetivo: Criar um sistema de mercado que permita ao usuário adicionar produtos ao carrinho, visualizar o carrinho, calcular o total e finalizar a compra.

from datetime import datetime
import time

operations = ["add", "remove", "cart", "clear", "calc", "wallet", "buy"]

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
    return f"R${n:2.2f}"

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

firstTime = False
while True:
    if not firstTime:
        print("==============================================")
        print("Seja bem-vindo a loja virtual do python\n")
        ops = "Operações: "
        ps = "Produtos Disponíveis:"

        for o in operations:
            ops += o + " "

        for pName, price in products.items():
            ps += f"\n- Nome: {pName.capitalize()}\n  Preço: {formatCurrency(price)}"

        print(ops + "\n" + ps)
        print("==============================================")
        
        firstTime = True

    #

    op = input("\nSelecione uma operação válida\n~ ")

    match op:
        case "add":
            itemName = input("\nDigite o nome do produto: ").lower()
            if itemName in products:
                cart.append(Product(itemName, products[itemName]))

                print(f"Produto '{itemName}' foi adicionado ao carrinho.")
            else:
                print(f"O produto '{itemName}' não foi encontrado. Digite um nome de produto válido")

        case "remove":
            itemName = input("\nDigite o nome do produto que deseja remover: ").lower()
            itemAmount = int(input("Digite a quantidade que deseja remover: "))

            if itemAmount < 0:
                raise ValueError("Quantidade inválida.")

            foundItems = 0
            i = 0
            for item in cart:
                if item.name == itemName:
                    foundItems += 1
                    del cart[i]
                else:
                    i += 1

                if foundItems == itemAmount:
                    break

            if foundItems >= 0:
                print(f"O produto '{itemName}' foi removido {itemAmount} vez{'es' if foundItems != 1 else ''} do carrinho.")
            else:
                print(f"O produto '{itemName}' não foi encontrado.")
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
            print(f"O preço total da compra é R${getTotalPrice():2.2f}")
        case "wallet":
            print(f"Seu saldo atual é de {formatCurrency(money)}")
        case "buy":
            if len(cart) == 0:
                print("O carrinho está vazio.")
                continue

            total = getTotalPrice()
            if money >= total:
                noteName = f"nota-{time.time_ns()}.txt"

                f = open(noteName, "x", encoding="utf8")
                f.write(
                    f"===============NOTA FISCAL===============\n{datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n\nPRODUTOS:\n"
                )
                for itemName, amount in getItemCount():
                    f.write(f"{itemName.upper()} x{amount} - {formatCurrency(products[itemName] * amount)}\n")
        
                f.write(
                    f"\nTOTAL: {formatCurrency(total)}\n" +
                    "========================================="
                )
                f.close()

                cart.clear()
                money -= total

                print(f"Compra efetuada com sucesso! seu saldo atual é de {formatCurrency(money)}")
            else:
                print("Saldo insuficiente.")
        case "exit":
            break
        case _:
            print("Operação inválida.")