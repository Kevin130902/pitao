class Arma: # (De brinquedo rs)
    __nome: str
    __cor: str
    __municao: list[int]

    def __init__(self, nome: str, cor: str, pentes_qtd: int, balas_por_pente: int):
        self.__nome = nome
        self.__cor = cor
        self.__municao = list(balas_por_pente for _ in range(pentes_qtd))

        print(f"Foi criada uma {nome} de cor {cor}.")

    def atirar(self):
        municao = self.__municao
        tamanho = len(municao)

        if tamanho > 0 and municao[tamanho - 1] > 0:
            municao[tamanho - 1] -= 1
            print("Pew! ", end=" ")
        else:
            print("As balas acabaram!")

    def recarregar(self):
        if len(self.__municao) - 1 >= 0:
            self.__municao.pop()

            print("Recarregado!")
        else:
            print("Sem munição!")

    def checar_municao(self):
        return len(self.__municao) > 0

    def checar_balas(self):
        return self.checar_municao() and self.__municao[len(self.__municao) - 1] > 0
    
    def set_nome(self, nome: str):
        self.__nome = nome

    def get_nome(self):
        return self.__nome

    def set_cor(self, cor: str):
        self.__cor = cor

    def get_cor(self):
        return self.__cor

arsenal = [
    ("Nerf Pistola", "Amarela", 10, 6),
    ("Nerf Metralhadora", "Verde", 20, 128),
    ("Nerf Shotgun", "Vermelha", 15, 48),
]

for detalhes in arsenal:
    arma = Arma(detalhes[0], detalhes[1], detalhes[2], detalhes[3])

    print(arma.get_nome() + ": ", end="")
    for _ in range(1000):
        if arma.checar_balas():
            arma.atirar()
        else:
            arma.recarregar()
            if not arma.checar_municao():
                print("Sem munição!")
                break

    print("\n")