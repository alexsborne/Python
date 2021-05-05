class Pessoa:
    def cumprimentar(self, num):
        return f"Olá {id(self)} , {num}"

    def contratar(self,contratado, ctps):
        print(f'Seja bem-vindo {contratado}, ctps: {ctps}')

if __name__ == '__main__':
    p = Pessoa()
    print(Pessoa.cumprimentar(p, 83))
    print(p.contratar('Alex', 123456798))


