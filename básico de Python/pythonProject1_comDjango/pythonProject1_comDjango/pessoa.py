class Pessoa:
    olhos = 2 #atributo default ou tb conhecido como atributo de classe

    def __init__(self, *filhos, nome=None, idade=None): #*filhos é um atributo que torna a classe um objeto complexo;
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)

    def cumprimentar(self, num=None):
        return f"Olá {id(self)} "

    def contratar(self,contratado, ctps):
        print(f'Seja bem-vindo {contratado}, ctps: {ctps}')

if __name__ == '__main__':
    renzo =   Pessoa(nome='Renzo')
    alex =    Pessoa (nome='Alex', idade = 34)
    luciano = Pessoa(renzo, alex, nome='Luciano', idade = 35)

    print(Pessoa.cumprimentar(luciano))
    print(id(luciano))
    print(luciano.nome)
    print(luciano.idade)
    print(luciano.filhos)
    luciano.sobrenome = 'Oliveira'
    print(luciano.__dict__)#mostra todos os atributos da instância do objeto
    print(alex.__dict__)#__dict__ só mostra abritutos de instância;
    del alex.idade #removeu o atributo dinamicamente
    print(alex.__dict__)
    print(alex.olhos)
    print(Pessoa.olhos)

    for filho in luciano.filhos:
        print(filho.nome)



