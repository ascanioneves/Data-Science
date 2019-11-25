import statistics
#from statistics import mean, median --> outra forma de importar
#from statistics import * --> acessa todas as funções da biblioteca

z = [10, 20, 20, 40]
x = statistics.mean(z) #média
y = statistics.median(z) #mediana

print(x,y)