# 1
# x, y = [int(i) for i in input("Insira dois nunmeros separados por espaço").split()]
# print(x if x > y else y)

# 2
# x = float(input("Digite um numero"))
# print("positivo" if x > 0 else ("negativo" if x < 0 else "neutro"))

# 3
# x = input("Digite seu sexo[F/M]")
# print("Feminino" if x == "F" or x == "f" else ("Masculino" if x == "M" or x == "m" else "Sexo inválido"))

# 4
# vogal = ['a', 'e', 'i', 'o', 'u']
# x = input("Digite uma letra")
# if len(x) > 1:
#     print("Será considerada só a primeira letra...")
# if x[0] in vogal:
#     print("Vogal")
# else:
#     print("Consoante")

# 5
# n1, n2 = [float(i) for i in input("Insira as duas notas parciais separadas por espaço").split()]
# m = (n1+n2)/2
# if m == 10:
#     print("Aprovado com Distinção")
# elif m >= 7:
#     print("Aprovado")
# else:
#     print("Reprovado")

# 6
# x, y, z = [int(i) for i in input("Insira tres numeros separados por espaço").split()]
# print(x if x > y and x > z else (y if y> x and y> z else z))

# 7
# x, y, z = [int(i) for i in input("Insira tres numeros separados por espaço").split()]
# print("maior {:d}".format(x if x > y and x > z else (y if y> x and y> z else z)))
# print("menor {:d}".format(y if x > y and z > y else (x if y> x and z> x else z)))

# 8
# x, y, z = [float(i) for i in input("Insira tres valores separados por espaço").split()]
# print("Compra o produto{:d}".format(2 if x > y and z > y else (1 if y > x and z > x else 3)))

# 9
# lst = [int(i) for i in input("Insira tres numeros separados por espaço").split()]
# lst = sorted(lst)
# for i in lst:
#     print(i, end=" ")

# 10
# t = input("Estuda em qual turno\ndigitar M-matutino ou V-Vespertino ou N-Noturno")
# if t == "M" or t == "m":
#     print("Bom dia")
# elif t == "V" or t == "v":
#     print("Boa Tarde")
# elif t == "n" or t == "n":
#     print("Boa Noite")
# else:
#     print("Op invalida")

# 11
dic = {"chave1": "Isso", "chave2": 'é', 1: 1, "chave3": "dicionário"}
print(dic["chave3"])
