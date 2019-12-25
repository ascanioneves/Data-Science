import pandas
from sklearn.model_selection import train_test_split #função que faz a divisão da base de dados

# ------ IRIS.CSV ------ #

iris = pandas.read_csv('iris.csv')
#print(iris['class'].value_counts()) #frequencia

# separando os registros da base de dados
# x guardara o primeiro parametro e y o terceiro
x, _, y, _ = train_test_split(iris.iloc[:, 0:4], iris.iloc[:, 4], test_size = 0.5, stratify = iris.iloc[:, 4])
#print(iris.iloc[:, 4])
print(x)
print(y.value_counts()) #separamos os registros cada um na metade, totalizando 75

# ------- IRIS.CSV ------ #

# ------- INFERT.CSV ------- #

infert = pandas.read_csv('infert.csv')
print(infert['education'].value_counts())

x1, _, y1, _ = train_test_split(infert.iloc[:, 2:9], infert.iloc[:, 1], test_size = 0.6, stratify = infert.iloc[:, 1])

print(y1.value_counts())

# ------- INFERT.CSV ------- #