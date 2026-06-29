#EXERCÍCIO 1 — LISTA
#Problema

#Crie um programa que:

#leia 5 nomes de alunos
#armazene em uma lista
#mostre todos os nomes no final


pessoa = {}

pessoa["nome"] = input("Digite o nome: ")

pessoa["idade"] = int(input("Digite a idade: "))

print("\nDados cadastrados:")

print("Nome:", pessoa["nome"])
print("Idade:", pessoa["idade"])
