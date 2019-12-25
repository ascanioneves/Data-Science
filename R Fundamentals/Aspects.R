getwd()

class(iris)

iristeste = iris
save(irisaux, file-"iristesteRdata")
rm(iristeste)
iristeste
load(file-"iristeste.Rdata")
iristeste


x = c(12,34,56,79)
y = c(1,6,9,14)

plot(x,y)

quit()