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
    luciano = Pessoa(renzo, alex, nome='Luciano')

    print(Pessoa.cumprimentar(luciano))
    print(id(luciano))
    print(luciano.nome)
    print(luciano.idade)
    print(luciano.filhos)
    luciano.sobrenome = 'Oliveira'
    print(luciano.__dict__)
    del alex.idade
    print(alex.__dict__)

    for filho in luciano.filhos:
        print(filho.nome)



