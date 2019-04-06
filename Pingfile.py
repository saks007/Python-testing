import os

#hostname = [ 'R1' , 'R2','R3']

f=open('ipadd')

for i in f:

    response = os.system("ping -c 1 " + i)
    #	os.system('clear')
    if response == 0:
        print(i, 'is up!')
    else:
        print(i, 'is down!')

f.close()