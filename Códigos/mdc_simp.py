number1=int(input('insert a number'))
number2=int (input('insert the second number'))
x=0
y=0
number=1
w=1


if number1==0 or number2==0:
    print(f'mdc ({number1}, {number2})= 0')

else:
    if number1>number2:
        x=number1
        y=number2
    else:
        x=number2
        y=number1
        
    if number1 % number2==0:
        print(f'mdc= {number2}')
       
    else:
        while number!=0:
            number=x % y
            w=y
            y=number
        
        print(f'mdc({number1}, {number2}) = {w}')