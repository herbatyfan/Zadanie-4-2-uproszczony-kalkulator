# zadanie 4.2
wyraz = []
lista1 = []
lista2 = []
wyraz = str(input())
for litera in wyraz:
     lista1.append(litera)
     lista2.append(litera)
lista2.reverse()
print(lista1 == lista2)
