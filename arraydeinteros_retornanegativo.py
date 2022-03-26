'''
 Crie um método que recebe um array de inteiros e retorna a quantidade de elementos
do array que são números negativos.
'''
numero_de_elementos=int(input('Quantos elementos você deseja inserir?'))
lista=[]
numeros_negativos=0

for i in range(numero_de_elementos):
    numero=int(input('insira o elemento desejado'))
    lista.append(numero)
    
for elemento in range(len(lista)):
    if lista[elemento]<0:
        numeros_negativos+=1
        
print(f' A quantidade de números negativos inseridas é igual a {numeros_negativos}')