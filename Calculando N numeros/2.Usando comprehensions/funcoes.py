from math import prod

def somar_lista(numeros):
    #podia apenas retornar sum(numeros) mas queria testar isso e deu certo KKKKK
    soma = sum([num for num in numeros])
    return soma

def multiplicar_lista(numeros):
    #infelizmente nao achei outra maneira e quis fazer parecido com o de cima
    # multi = prod(numeros)
    # return multi
    multi = prod([num for num in numeros])
    return multi

def duplicados_lista(numeros):
    #Talvez desse para melhorar o exercicio 1 e usei set para nao repetir o numero repetido varias vezes
    repetidos = set([num for num in numeros if numeros.count(num) > 1])
    return list(repetidos)

def impares_lista(numeros):
    impares = set([num for num in numeros if num % 2 != 0])
    return list(impares)

def pares_lista(numeros):
    pares = set([num for num in numeros if num % 2 == 0])
    return list(pares)

def primos_lista(numeros):
    primos = set([num for num in numeros if num > 1 and all(num % i != 0 for i in range(2, num))])                      
    return list(primos)

   