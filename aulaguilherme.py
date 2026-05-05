from random import randint

"""
recebe um número mínimo digitado pelo usuário
recebe um número máximo digitado pelo usuário. Caso seja menor que o mínimo, chama a função novamente.
gera um número aleatório entre o número mínimo e o número máximo. Se eles forem iguais retorna o número do mínimo (que é igual ao máximo).
"""

def gerar_min() -> int:
    minimo = int(input("Digite o número mínimo: "))
    return minimo

def gerar_max() -> int:
    maximo = int(input("Digite o número máximo: "))
    if maximo < minimo:
        print('Você não pode escolher um número menor que o mínimo')
        gerar_max()
    return maximo


def gerar_num(minimo: int, maximo: int) -> int:
    if minimo == maximo:
        return minimo
    return randint(minimo,maximo)

minimo = gerar_min()
maximo = gerar_max()
numero_aleatorio = gerar_num(minimo, maximo)
print(numero_aleatorio)