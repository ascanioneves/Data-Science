lst = [5,2,1,3,4,5,6,1,1,2] #lista de inteiros
lst.sort() #ordena a lista crescentemente
print(lst)

lst2 = [1,2,'string', True] #lista de inteiros, string e booleano
print(lst2)

lst3 = [1,2,[4,5,6],"a"] #lista de inteiros, outra lista e string
print(lst3[2][1]) #acessando o 5

lst4 = list(range(0,10))
print(lst4)

# AQUI VEM A PARTE DE PERCORRER A LISTA #

for i in range(len(lst)):
  print(lst[i])