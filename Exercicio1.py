# Exercícios INPUT e OUTPUT
# 1-

print("Olá Formador João Câncio!")

# 2-

print("Indique o seu nome: ")
nome = input()

print("Indique a sua idade: ")
idade = input()

print(f"{nome}, {idade} anos.")

# Exercícios Variáveis
# 1-

# (5) “Casa”
# (3) 2 + 0j
# (4) True
# (5) ‘123’
# (2) 1.2345
# (4) False
# (5) ‘’’2j’’’
# (3) 10 +1j
# (1) 2
# (5) ‘Programando Ideias’

# 2-

nome = input("Indique o seu nome: ")
nota = input("Indique a nota da prova de programação: ")

print(f"O {nome} tirou {nota} na prova de progrmação.")

# 1-

num1 = float(input("Indique a primeira nota: "))
num2 = float(input("Indique a segunda nota: "))
num3 = float(input("Indique a terceira nota: "))
num4 = float(input("Indique a quarta nota: "))

print(f"A média das notas é {(num1 + num2 + num3 + num4) / 4}")

# 2-

temp = float(input("Indique a temperatura atual em ºC: "))

print(f"A temperatura em ºF é de {temp * 1.8 + 32} e em K é de {temp + 273.15}")

# 3-

corCabelo = input("Indique a cor do cabelo da personagem: ")
corPele = input("Indique a cor de pele da personagem: ")
classe = input("Indique a classe da personagem: ")
idade = int(input("Indique a idade da personagem: "))
altura = float(input("Indique a altura da personagem: "))
habilidade = input("Indique a habilidade especial da personagem: ")

print(f"A personagem tem o cabelo {corCabelo}, cor de pele {corPele}, classe {classe}, tem {idade} anos, {altura}m de altura e usa {habilidade} como habilidade especial.")
