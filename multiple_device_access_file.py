import getpass
import sys
import telnetlib

	
user = raw_input("Enter your remote account: ")
password = getpass.getpass()

f=open('ipadd')
for l in f:
    print('configuring switch with ' + l +'\n')
    HOST=l
	tn = telnetlib.Telnet(HOST)

	tn.read_until("Username: ")
	tn.write(user + "\n")
	if password:
   		tn.read_until("Password: ")
    	tn.write(password + "\n")


	tn.write("conf t\n")

	t=input('how many loopback interfaces would like to create:')
	x=input('from which range:')
	k=x+t

	p=raw_input('IP SUBMET:')
		
	for i in range(x+1,k+1):
		tn.write("int lo" + str(i) + "\n")
		tn.write("ip add " + str(p) + str(i) + " 255.255.255.0 \n")

	tn.write("end\n")
	tn.write("wri\n")


	tn.write("exit\n")

print tn.read_all()
