# Questao 02

x = 0
lista = []
while x < 25:
    num = int(input())
    lista.append(num)
    x+=1
print(lista)
lista.sort()
print("maior = {}".format(lista[24]))
print("menor = {}".format(lista[0]))
y = 0
for i in lista:
    y += i
k = y/5
print("A media dos elementos da lista é = {}".format(k))
print("A mediana dos elementos da lista é = {}".format(lista[12]))
