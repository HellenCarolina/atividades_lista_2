#Faça um programa que converta metros para centimetros.
#1m tem 100cm
#entrada
tamanho_em_metros= float (input('Digite o tamanho em metros:'))

#calculos 
tamanho_em_centimetros = tamanho_em_metros* 100

#exibir 
print ('{} metros e igual a {:.0f}centimetros'. format(tamanho_em_metros,tamanho_em_centimetros))