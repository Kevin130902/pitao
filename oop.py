class Arma: # (De brinquedo rs)
    nome: str
    cor: str
    pentes_iniciais: int
    balas_por_pente: int

    municao: list[int]

    def __init__(self, nome: str, cor: str, pentes_qtd: int, balas_por_pente: int):
        self.nome = nome
        self.cor = cor
        self.pentes_iniciais = pentes_qtd
        self.balas_por_pente = balas_por_pente

        self.municao = list(self.balas_por_pente for _ in range(pentes_qtd))

        print(f"Foi criada uma {nome} de cor {cor}.")

    def atirar(self):
        municao = self.municao
        tamanho = len(municao)

        if tamanho > 0 and municao[tamanho - 1] > 0:
            municao[tamanho - 1] -= 1
            print("Pew! ", end=" ")
        else:
            print("As balas acabaram!")

    def recarregar(self):
        if len(self.municao) - 1 >= 0:
            self.municao.pop()

            print("Recarregado!")
        else:
            print("Sem munição!")

    def checarMunicao(self):
        return len(self.municao) > 0

    def checarBalas(self):
        return self.checarMunicao() and self.municao[len(self.municao) - 1] > 0

arsenal = [
    ("Nerf Pistola", "Amarela", 10, 6),
    ("Nerf Metralhadora", "Verde", 20, 128),
    ("Nerf Shotgun", "Vermelha", 15, 48),
]

for detalhes in arsenal:
    arma = Arma(detalhes[0], detalhes[1], detalhes[2], detalhes[3])

    print(arma.nome + ": ", end="")
    for _ in range(1000):
        if arma.checarBalas():
            arma.atirar()
        else:
            arma.recarregar()
            if not arma.checarMunicao():
                print("Sem munição!")
                break

    print("\n")