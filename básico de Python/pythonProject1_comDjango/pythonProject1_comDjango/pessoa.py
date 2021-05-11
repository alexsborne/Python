class Pessoa:
    def __init__(self, *filhos, nome=None, idade=None):
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)

    def cumprimentar(self, num=None):
        return f"Olá {id(self)} "

    def contratar(self,contratado, ctps):
        print(f'Seja bem-vindo {contratado}, ctps: {ctps}')

if __name__ == '__main__':
    renzo =   Pessoa(nome='Renzo')
    alex =    Pessoa (nome='Alex')
    alex1 =    Pessoa (nome='Alex')
    alex2 =    Pessoa (nome='Alex')

    luciano = Pessoa(renzo, alex, alex1, alex2, nome='Luciano')

    print(Pessoa.cumprimentar(luciano))
    print(id(luciano))
    print(luciano.nome)
    print(luciano.idade)
    print(luciano.filhos)

    for filho in luciano.filhos:
        print(filho.nome)



