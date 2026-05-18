def soma(valor1,valor2,valor3):
    v_soma = valor1 + valor2 + valor3
    return v_soma
if __name__ == '__main__':
    valor1=int(input("Primeiro valor:"))
    valor2=int(input("Segundo valor:"))
    valor3=int(input("Terceiro valor:"))
    v_retorno= soma(valor1,valor2,valor3)
    print("Soma =", v_retorno)