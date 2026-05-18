#Crie uma função para subtrair dois valores. Ele recebe os valores, calcula a subtração e retorna o resultado do calculo.
def sub(valor1, valor2):
    v_sub = valor1 - valor2
    return v_sub
if __name__ == '__main__':
    valor1 = int(input("Digite o primeiro valor:"))
    valor2 = int(input("Digite o segundo valor:"))
    v_retorno = sub(valor1, valor2)
    print ("Subtração =", v_retorno)