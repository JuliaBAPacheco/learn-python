import math

number=int(input('insert a number'))
x= math.ceil(math.sqrt(number))
divisor=0

for i in range (1,x+1):
    reminder=number%i
    
    if reminder==0:
        divisor+=1 # divisor = divisor + 1
        
if divisor==1:
    print('the number is prime')
else:
    print('the number isn\'t prime')
        