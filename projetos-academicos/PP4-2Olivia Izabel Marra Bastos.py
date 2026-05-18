ct = 0
print("Ordem decrescente:")
valor_inicial = int(input("Digite o valor inicial:"))
for numero in range(valor_inicial, -1, -1):
    print(numero)
    ct = ct + 1
print("Quantidade de valores:", ct)