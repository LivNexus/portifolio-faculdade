ct = 0
soma = 0
print("Números inteiros de 1 a 500:")
for numero in range(1, 500 + 1, 1):
    ct = ct + 1
    soma = soma + ct
print("Quantidade de valores:", ct)
print("Soma dos valores:", soma)