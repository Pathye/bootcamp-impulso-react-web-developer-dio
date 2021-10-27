# Função: Buscar posiçao do nome e altura no vetor
# Autor: Patrícia Yalmanian Fernandes Pedrosa

nome = ['Lucas', 'Pedro', 'Rafael', 'Hugo', 'Fabio']
altura = ['1.76', '1.88', '1.66', '1.73', '1.79']
i = 0

print("+---------------------+")
print("|       TABELA        |")
print("+---------------------+")

for i in range(5):
    print(nome[i], '\t\t', "|" ,altura[i])
