#Minha resolução

escreva = input ( 'Escreva algo: ' )

print ('O tipo primitivo é: ', type(escreva) )

print ('É numérico? ', escreva.isnumeric()  )
print ('É alfabético? ', escreva.isalpha()  )
print ('É alphanumérico? ', escreva.isalnum() )
print ('Sem Informação: ', escreva.isspace() )
print ('Só letras minusculas: ', escreva.islower() )
print ('Só letras maiusculas: ', escreva.isupper() )
print ('Letras maiusculas e minusculas(Capitalizada): ', escreva.istitle() )