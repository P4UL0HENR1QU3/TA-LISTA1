from funcoes import (somar_lista, multiplicar_lista, duplicados_lista, impares_lista, pares_lista, primos_lista)

def exibir_resultados(numeros):
    exibir_soma = somar_lista(numeros)
    exibir_multi = multiplicar_lista(numeros)
    exibir_duplicados = duplicados_lista(numeros)
    exibir_impares = impares_lista(numeros)
    exibir_pares = pares_lista(numeros)
    exibir_primos = primos_lista(numeros)
    print(f"Calculo da soma dos numeros inteiros: {exibir_soma}")
    print(f"Calculo da multiplicacao dos numeros inteiros: {exibir_multi}")
    print(f"Exibicao dos numeros inteiros duplicados/repetidos: {exibir_duplicados}")
    print(f"Exibicao dos numeros inteiros impares: {exibir_impares}")
    print(f"Exibicao dos numeros inteiros pares: {exibir_pares}")
    print(f"Exibicao dos numeros primos: {exibir_primos}")

def exibir_pergunta(numeros=None):
    if numeros is None:
        numeros = []

    try:
        numero = int(input("Digite um número inteiro (0 para parar): "))
        if numero == 0:
            print(f"Numeros digitados: {numeros}")
            exibir_resultados(numeros)
            numeros.append(numero)
            return numeros
        else:
            numeros.append(numero)
            return exibir_pergunta(numeros) 
    except ValueError:
        print("Coloque um valor inteiro")
        return exibir_pergunta(numeros)

def main():

    exibir_pergunta()

if __name__ == "__main__":
    main()