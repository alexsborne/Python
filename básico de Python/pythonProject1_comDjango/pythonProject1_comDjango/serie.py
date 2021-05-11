class Serie:
    def __init__(self, nome, ano, temporadas):
        self.nome= nome
        self.ano = ano
        self.temporadas = temporadas

serie = Serie('O Inocente', 2018, 15)
print(serie.nome)
print(serie.ano)
print(serie.temporadas)