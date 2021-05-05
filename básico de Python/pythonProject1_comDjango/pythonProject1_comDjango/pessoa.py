class Pessoa:
    def __init__(self, nome=None, idade=None):
        self.nome = nome
        self.idade = idade

    def cumprimentar(self, num):
        return f"Olá {id(self)} , {num}"

    def contratar(self,contratado, ctps):
        print(f'Seja bem-vindo {contratado}, ctps: {ctps}')

if __name__ == '__main__':
    p = Pessoa('Alex')
    print(p.nome)

    #print(Pessoa.cumprimentar(p, 83))
    #print(p.contratar('Alex', 123456798))
    print(p.nome)
    p.nome = "Renzo"
    p.idade = 35
    print(f'{p.nome}, {p.idade}')



