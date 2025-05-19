from math import prod

def somar_lista(numeros):
    #podia apenas retornar sum(numeros) mas queria testar isso e deu certo KKKKK
    soma = sum([num for num in numeros])
    return soma

def multiplicar_lista(numeros):
    #infelizmente nao achei outra maneira e quis fazer parecido com o de cima
    multi = prod([num for num in numeros])
    return multi
    # multi = prod(numeros)
    # return multi

def duplicados_lista(numeros):
    verificar = []
    repetidos = set()

    for i in numeros:
        if i not in verificar:
            verificar.append(i)
        else:
            repetidos.add(i)

    return list(repetidos)

def impares_lista(numeros):
    impares = []
    for i in numeros:
        if i % 2 != 0 and i not in impares:
            impares.append(i)

    return list(impares)

def pares_lista(numeros):
    pares = []
    for i in numeros:
        if i % 2 == 0 and i not in pares:
            pares.append(i)
        
    return list(pares)

def primos_lista(numeros):
    primos = []

    for numero in numeros:
        primo = 1

        for i in range(2, numero):
            if numero % i == 0:
                primo = 0
                break

        if primo == 1 and numero > 1 and numero not in primos:
            primos.append(numero)

    return list(primos)