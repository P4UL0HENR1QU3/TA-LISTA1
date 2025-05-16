frase = str(input("Coloque uma frase: "))
if frase.isdigit():
    print("Digite uma frase, não um número")

frase_maiusculo = frase.title()

print(f"{frase} -> {frase_maiusculo}")

