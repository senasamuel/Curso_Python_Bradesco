qtd =0
soma =0
media=0
valor = float(input("Digite um valor: "))

while (valor > 0.0):
    soma = soma + valor
    qtd = qtd + 1
    #Entraada de valor
    valor = float(input("Digite um valor:"))

#Caso digite um valor negativo o laço encerra
media = soma / qtd
print("\n Total da Soma:" ,soma )
print("\n Quatidade de valor digitados:",qtd)
print("\n Média dos valores:", media)