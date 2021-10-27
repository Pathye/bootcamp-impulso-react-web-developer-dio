# Função: Acessar menu de opções
# Autor: Patrícia Yalmanian Fernandes Pedrosa

menu = 0

print("Menu de acesso: 1 - Netflix | 2 - Youtube | 3 - Globoplay | 4 - Sair")
menu = int(input("Digite sua opção: "))

if (menu == 1):
    print("Conectando á Netflix")
elif (menu == 2):
    print("Conectando á Youtube")
elif (menu == 3):
    print("Conectando á Globoplay")
elif (menu == 4):
    print("Saindo do menu... Até mais!")
else:
    print("Acesso inválido")
