ct = 0
print("Ordem crescente:")
valor_final = int(input("Digite o valor final:"))
for numero in range(0, valor_final + 1, 1):
    print(numero)
    ct = ct + 1
print("Quantidade de valores:", ct)