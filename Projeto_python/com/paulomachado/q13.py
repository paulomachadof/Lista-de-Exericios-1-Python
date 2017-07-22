'''
Created on 22 de jul de 2017

@author: Paulo-PC
'''
print("Qual seu sexo? 1.Feminino 2. Masculino")
sexo = int(input())

print("Qual sua altura: ")
alt = float(input())

print("Qual seu peso: ")
peso = float(input())

if sexo == 1:
    peso_ideal = (62.1*alt) - 44.7
    print("Seu peso ideal eh ",peso_ideal)
    if peso > peso_ideal:
        print("Voce esta acima do peso")
else:
    peso_ideal = (72.7*alt) - 58
    print("Seu peso ideal eh ",peso_ideal)
    if peso > peso_ideal:
        print("Voce esta acima do peso")