import calc

x=int(input('which calculator function would you like to do now? \n 1  for addition \n 2 for sub \n 3 for mul \n 4 for divition:'))

y=int(input('enter value for A:'))
z=int(input('enter value for B:'))

if x==1:
    t=calc.add(y,z)
elif x==2:
          t=  calc.sub(y,z)
elif x==3:
           t= calc.mul(y,z)
elif x==4:
        t=    calc.div(y,z)


print('the result is :', t)