def soma(a, b):
  return a + b

def imprimir(msg):
  print(msg)

def potencia(base, exp):
  return base ** exp

def printarIntervalo(inicio = 1, fim = 10):
  for i in range(inicio, fim):
    print(i)

a = int(input())
b = int(input())

# ---------------- > #
ans = soma(a,b)
print(ans)
# ---------------- > #

#imprimir("Esta mensagem vai ser impressa")

# ---------------- > #
base = int(input())
exp = int(input())
# ---------------- > #

# ---------------- > #
pot = potencia(base, exp)
print(pot)
# ---------------- > #

printarIntervalo()
