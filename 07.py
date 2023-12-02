n1=input('Digite algo aqui:')
print('O tipo do dado inserido é: {}'.format(type(n1)))
print('O dado inserido é numérico, ou seja, contém apenas números:{}'.format(n1.isnumeric()))
print('O dado inserido é alfabético, ou seja, contém apenas letras:{}'.format(n1.isalpha()))

print('O dado inserido é alfanumérico, ou seja, contém apenas letras e/ou números:{}'.format(n1.isalnum()))

print('O dado inserido possui todas as letras em maiúsculo:{}'.format(n1.isupper()))
print('O dado inserido possui todas as letras em minúsculo:{}'.format(n1.islower()))
print('O dado inserido possui a primeira letra em maiúsculo:{}'.format(n1.istitle()))
print('O dado inserido possui apenas espaços em branco:{}'.format(n1.isspace()))