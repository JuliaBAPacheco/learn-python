'''Crie um método que recebe um array de inteiros a e um valor inteiro x e retorna a
quantidade de vezes que x aparece no array a.'''

quantidade_de_elementos=int(input('Quantos elementos você deseja inserir'))
x=int(input('Qual valor deseja encontrar na lista?'))
lista=[]
numero_desejado=0

for i in range (quantidade_de_elementos):
    numero=int(input('insira os elementos da lista desejada'))
    lista.append(numero)
    
for elemento in lista:
    if elemento==x:
        numero_desejado+=1

print(f' A quantidade de vezes que o número {x} aparece na lita é igual a {numero_desejado}')