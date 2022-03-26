''' Exercício 7: Escreva um método que recebe um array de números e devolve a posição onde se
encontra o maior valor do array. Se houver mais de um valor maior, devolver a posição da primeira
ocorrência.'''

numero_de_elementos=int(input('Quantos elementos deseja inserir?'))
lista= []
for i in range (numero_de_elementos):
    numero=int(input('insira o número desejado'))
    lista.append(numero)
    
print(lista)
maior_elemento=lista[0]
p=0
    
for posicao in range(len(lista)):
    if maior_elemento<lista[posicao]:
        maior_elemento=lista[posicao]
        p=posicao
       
print(maior_elemento)
print(p)