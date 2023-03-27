print('Seja bem-vindo ao simulador de investimentos\n')

cap = float(input('Quanto você tem para investir hoje?: '))
ap = float(input('Aplicação mensal: '))
n = int(input('Por quantos meses?: '))
i = float(input('Rentabilidade ao ano (%): '))

#Transformando taxa anual para mensal.
#Formula: i=((FV/PV)^(1/n))-1

ifv = 1*((1+(i/100))**1)

iq = ((ifv/1)**(1/12)-1)
      
#Formula: PV*((i+i)^n)
fv1 = cap*((1+iq)**n)

#Formula: PMT*((((1+i)^n)-1)i)
fv2 = ap*((((1+iq)**n)-1)/iq)


#Formula Geral: (PV*((i+i)^n))+(PMT*((((1+i)^n)-1)i))
fvsoma = fv1+fv2
                                

print('\nValor Total Acumulado R$ {:.2f}'.format(fvsoma))

sair = input('Você desejar sair? (s/n)')

#Adicionar estrutura de repetição While usando (s/n)
