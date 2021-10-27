# Função: Calcular média de notas e informar se foi apravado
# Autor: Patrícia Yalmanian Fernandes Pedrosa

aluno = ('')
n1 = 0
n2 = 0
n3 = 0
n4 = 0
n5 = 0

aluno = str(input("Digite o nome do aluno: "))

n1 = int(input("Digite a primeira nota: "))
n2 = int(input("Digite a segunda nota: "))
n3 = int(input("Digite a terceira nota: "))
n4 = int(input("Digite a quarta nota: "))
n5 = int(input("Digite a quinta nota: "))

media = (n1 + n2 + n3 + n4 + n5) / 5

print(f"A média de notas do aluno ", aluno ," é de: ", + media)

if (media >= 7 and media < 10):
    print("Você foi aprovado. Parabéns!")
elif (media == 10):
    print("Você foi aprovado com a melhor nota. Parabéns, continue assim!!")
else:
    print("Sinto muito. Você foi reprovado :(")
