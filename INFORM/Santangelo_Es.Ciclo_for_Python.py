nnumeri=int(input('quanti numeri vuoi inserire'))
lista=[]
prodotto=1
for i in range(nnumeri):
    numero = int(input('inserisci il numero: '))
    lista.append(numero)

for numero in lista:
    prodotto=prodotto*numero

print(prodotto)
    
    
