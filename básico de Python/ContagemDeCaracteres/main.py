
texto = input('Digite o texto: ')
texto = texto.replace(' ','');
lista_caracteres = sorted(texto.strip().upper())
contagem = 1
letra_anterior = lista_caracteres[0]
i = 1

for item in lista_caracteres[0:3]:
    print(item)

while i < len(lista_caracteres):
    if letra_anterior == lista_caracteres[i]:
        letra_anterior = lista_caracteres[i]
        contagem += 1
        i+=1
    else:
        print(f'{letra_anterior}: {contagem}')
        letra_anterior = lista_caracteres[i];
        contagem = 1
        i+=1
print(letra_anterior +': ' + contagem.__str__())

