notaA = float(input("Digite a primeira nota: "))
notaB = float(input("Digite a segunda nota: "))

#Calcular a média
mediaFinal = (notaA + notaB) / 2

#Verificação da média
if mediaFinal >= 7:
    print("A média: %.1f - Aprovado "% mediaFinal)
else:
    print("A média: %.1f - Reprovado "% mediaFinal)

# #Outro Exemplo 

# idade = int(input("Digite a idade da pessoa: "))
# if idade > 18:
#     print("Maior de idade")
# elif idade <= 16:
#     print("Infanto juvenil")
# else:
#     print("Menor de idade")