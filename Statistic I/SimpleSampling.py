import pandas
import numpy

base = pandas.read_csv('iris.csv') #data base

#print(base)

#creating a sampling
#parameters of random.choice(): numbers that you want to randomize in array format, size of sampling, replace, probabillity of each number  

#Use this method when you want to keep the sampling result. Note : You can put any value for this.
#numpy.random.seed(123)
amostra = numpy.random.choice(a = [0, 1], size = 150, replace = True, p = [0.5, 0.5])
print(amostra)
print('The total length of sampling : ', len(amostra))
print('The length of 0 list : ', len(amostra[amostra == 0]))
print('The length of 1 list : ', len(amostra[amostra == 1]))
