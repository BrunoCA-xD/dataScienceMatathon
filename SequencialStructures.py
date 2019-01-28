import math
# 1
print("hello Word")

# 2
# x = input("Input a number")
# print("The number its {:.2f}".format(float(x)))

# 3
# num1, num2 = input("insert two numbers, separated by ',' :\n").split(",")
# print(float(num1)+float(num2))

# 4
# g0, g1, g2, g3 = input("insert four grades, separated by blank :\n").split(" ", 4)
# print((float(g0)+float(g1)+float(g2)+float(g3))/4)

# 5
# metre = float(input("Insira os metros para conversão\n"))
# print(metre*100)

# 6
# r = float(input("Insira o raio do circulo\n"))
# a = math.pi * math.pow(r, 2)
# print("area = {:.2f}cm²".format(a))

# 7
# ld = float(input("Insira 1 lado do quadrado\n"))
# print("area: {:.2f}\ndobro da area: {:.2f}".format(ld*ld, ld*ld*2))

# 8
# sh = float(input("insira seu salario/hora"))
# ht = float(input("insira a quantidade de horas trabalhadas"))
# print("salario: {:.2f}".format(sh*ht))

# 9
# f = float(input("insira a temperatura em Farenheit "))
# c = (5 * (f-32) / 9)
# print("Cº: {:.2f}".format(c))

# 10
# c = float(input("insira a temperatura em Cº "))
# f = (c * 9/5) + 32
# print("Farenheit: {:.2f}".format(f))


# 11 -- inputs
# int1, int2 = [int(i) for i in input("Insira dois numeros inteiros separados por espaço\n").split()]
# real = float(input("Insira um numero real\n"))
# -- A
# respostaA = 2*int1 * float(int2/2)
# print(respostaA)
# -- B
# respostaB = 3*int1 + real
# print(respostaB)
# -- C
# respostaC = math.pow(real, 3)
# print(respostaC)

# 12
# a = float(input("Insira sua altura para saber seu peso ideal:\n"))
# p = (72.7 * a) - 58
# print("Seu peso ideia seria:{:.2f}".format(p))

# 13 -- A e B
# a = float(input("Insira sua altura para saber seu peso ideal:\n"))
# print("Seu peso ideia seria:{:.2f} se fosse homem e:{:.2f}".format((72.7 * a) - 58,  (62.1*a) - 44.7))

# 14
# peso = float(input("Insira o peso em KG dos peixes pescados\n"))
# pesoE = peso-50.0 if peso >= 50.0 else 0
# multa = pesoE * 4.00
# print("Peso excedente: {:.2f}\nMulta: R${:.2f}".format(pesoE, multa))

# 15 -- inputs
# sh, ht = [float(i) for i in input("Insira seu salario/hora e as horas trabalhas separados por espaço:\n").split()]
# a
# sb = sh*ht
# b
# ir = 0.11 * sb
# c
# inss = 0.08 * sb
# d
# sindicato = 0.05 * sb
# E
# print("+ Salário Bruto: {:.2f}R$".format(sb))
# print("- IR (11%): {:.2f}R$".format(ir))
# print("- INSS (8%): {:.2f}R$".format(inss))
# print("- Sindicato (5%): {:.2f}R$".format(sindicato))
# print("= Salário Liquido: {:.2f}R$".format(sb-ir-inss-sindicato))

# 16
# metros = float(input("Insira quantos m² você precisa pintar"))
# latasTinta = math.ceil(metros/(18*3)) if metros >= (18*3) else 1
# valor = 80.0 * latasTinta
# print("Latas necessarias:{:d}\nValor total:{:.2f}".format(latasTinta, valor))

# 17
# metros = float(input("Insira quantos m² você precisa pintar"))
# latasTinta18 = math.ceil(metros/(18*6)) if metros >= (18*6) else 1
# latasTinta = math.ceil(metros/(3.6*6)) if metros >= (3.6*6) else 1
# miscL = 0
# miscG = math.ceil(metros/(3.6*6)) if (0.5 * metros) >= (3.6*6) else 1
#
# if miscG >= 5:
#     miscL += miscG//5*1
#     miscG -= miscG//5*5
# valor18 = 80.0 * latasTinta18
# valor = 25 * latasTinta
# valorMisc = 80.0 * miscL + 25.0 * miscG
#
# print("Latas necessarias de 18 litros:{:d}".format(latasTinta18))
# print("Valor:{:.2f}".format(valor18))
# print("Galões necessarios de 3,6 litros:{:d}".format(latasTinta))
# print("Valor:{:.2f}".format(valor))
# print("misc... galões:{:d} - latas:{:d}".format(miscG, miscL))
# print("ValorTotal:{:.2f}".format(valorMisc))

# 18

arq = float(input("Insira o tamanho do arquivo em MB"))
link = float(input("Insira a velocidade da sua internet em Mbps"))
link = link * 0.125

print("{:.2f} minutos".format(arq/link/60))
