def lerNotas():
    n = float(input("Digite uma nota para o aluno(a): "))
    return n

def resultado (n1, n2):
    media = (n1 + n2) / 2
    print("Nota 1: ", n1)
    print("Nota 2: ", n2)
    print("Média: ", media, "\t Resultado: ", end="")
    if media >= 7:
        print("Aprovado")
    else:
        print("Reprovado")

a = lerNotas()
b = lerNotas()
resultado(a, b)