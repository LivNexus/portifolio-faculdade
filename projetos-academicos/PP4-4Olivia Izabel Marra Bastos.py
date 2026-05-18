ct = 0
soma = 0
print("Números inteiros de 1 a 500:")
for impar in range(1, 500 + 1, 2):
    ct = ct + 1
    soma = soma + impar
print("Quantidade de valores:", ct)
print("Soma dos impares:", soma)
