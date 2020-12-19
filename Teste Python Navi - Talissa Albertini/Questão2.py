import math
import numpy

i=0
lista = [0]*10
while i < 10 :
    if i%2 == 0:
        lista[i] = (3**i)+ 7*(math.factorial(i))
    else:
        lista[i] = (2**i)+ 4*(math.log(i))
    i+=1
print(lista)

#encontrar a posição do maior valor 
maior_valor = max(lista)
posicao_maior_valor = lista.index(maior_valor)
print(posicao_maior_valor)

#média dos valores (2 casas decimais)
media = numpy.mean(lista)
print(f'A média dos elementos da lista é igual a {media:.2f}')

