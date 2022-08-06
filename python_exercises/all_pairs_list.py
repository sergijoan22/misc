
lista = [4,6,3]

for i in range(len(lista)):
    for j in range(i, len(lista)):
        if i != j:
            print(f'{lista[i]} y {lista[j]}')
