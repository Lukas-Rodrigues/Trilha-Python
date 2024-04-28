texto = 'Lucas'
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra,end="")


print("\n-------------------------------")
#exibindo a tabuada de  5 

for numero in range(0,51,5):
    print(numero,end="")