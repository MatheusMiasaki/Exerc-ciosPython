altura = float (input ('Indique a altura da parede: '))
comp = float (input ('Indique o comprimento da parede: '))

area = altura*comp 

print ('A área é de {:.3f} Metros quadrados'.format (area))

tinta = area / 2

print (40*'=')

print ('Você gastará {:.3f} litros de tinta'.format (tinta))