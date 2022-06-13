print('Bem vindo a sua nova calculadora!')

x = int(input('Digite um numero: '))
print()
 

oper = str(input('Digite o simbolo da operação(+, -, * ou /)'))
print()

y = int(input('Digite outro numero: '))
print()
    

if oper == ('+'):
    print ("O total da soma é de: ", (x + y))
    
elif oper == ('-'):
    print ("O total da subtração é de: ", (x - y))
    
elif oper == ('*'):
    print ("O total da multiplicação é de: ", (x * y))
    
elif oper == ('/'):
    print ("O total da divisão é de:", (x / y))
    
elif oper != ('+') or ('-') or ('*') or ('/'):
    print ("operação inválida")
    
else:
    print ('baita arrombado tu hein guri')