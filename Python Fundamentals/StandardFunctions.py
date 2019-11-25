from statistics import *
from numpy import *

print(abs(-100)) #valor absoluto

lista = [5, 2, 3, 1, 9]
print(max(lista)) #imprime o maior valor da lista
print(sum(lista)) #imprime a soma da lista
print(min(lista)) #imprime o menor valor da lista

print("Media : ", mean(lista)) #imprime a média da lista
print("Mediana : ", median(lista)) #imprime a mediana da lista

a = random.random((8,8)) #gera uma matriz 8 por 8 aleatória
print(a)