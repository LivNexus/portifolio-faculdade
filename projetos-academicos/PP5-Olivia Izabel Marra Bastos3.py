from datetime import datetime
def ano(valor_ano):
    idade = datetime.now().year - valor_ano
    return idade
if __name__ =='__main__':
    valor_ano = int(input("Digite o seu ano de nascimento:"))
    v_retorno = ano(valor_ano)
    print("Sua idade é", v_retorno, 'anos')