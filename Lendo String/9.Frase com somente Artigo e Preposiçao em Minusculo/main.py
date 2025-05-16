frase = str(input("Coloque uma frase: "))
if frase.isdigit():
    print("Digite uma frase, não um número")

frase_diminutivo = frase.lower()
separar_palavras = frase_diminutivo.split()

artigos_e_prep = ["a", "ante", "após", "até", "com", "contra", "de", "desde", "em", "entre", "para", "perante", "por", "sem", "sob", "sobre", "trás",
"o", "a", "os", "as", "é", "um", "uma", "uns", "unas"]

frase_verificada = []

for palavra in separar_palavras:
    if palavra in artigos_e_prep:
        frase_verificada.append(palavra)
    else:
        frase_verificada.append(palavra.capitalize())

exibir_frase = " ".join(frase_verificada) #junta uma lista de string numa frase
print(exibir_frase)


