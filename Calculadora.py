print(' ')
print(' ')
print('==================<<<   C A L C U L A D O R A   >>>==================')
print(' ')
print(' ')
number_1 = int(input('Enter your first number.: '))
number_2 = int(input('Enter your second number: '))
operacao = input('''Entre com a operação....: ''')
print(' ')
print(' ')
if   operacao == '+':
   result = number_1 + number_2
elif operacao == '-':
   result = number_1 - number_2    
elif operacao == '*':
   result = number_1 * number_2       
elif operacao == '/':
   result = number_1 / number_2       

print('O resultado da operação é: ',result)
print('FIM!!!')
