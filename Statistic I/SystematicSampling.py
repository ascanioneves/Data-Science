import pandas 
import numpy
from math import ceil

#Até o momento não existe uma função pronta para amostragem sistemática em python, então vamos implementar a função

populacao = 150
amostra = 15
k = ceil(populacao / amostra) #arredondamento pra cima

rand = numpy.random.randint(low = 1, high = k + 1, size = 1) #gerando um numero aleatório entre 1 e k no formato de vetor

acumulador = rand[0] # O inteiro sorteado
sorteados = [] # Lista vazia

for i in range(amostra):
  #print(acumulador)
  sorteados.append(acumulador)
  acumulador += k
#print(sorteados)

base = pandas.read_csv('iris.csv')
baseFinal = base.loc[sorteados] # Fará a indexação de acordo com a lista gerada aleatoriamente.

#Técnica : Amostragem Sistemática

print(baseFinal)
