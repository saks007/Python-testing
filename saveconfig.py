import getpass
#import sys
import telnetlib

# Get Username and Password
user = raw_input("Enter your username: ")
password = getpass.getpass()

#  Open file with list of switches
f = open ("ipadd")

#  Telnet to each switch and cofigure it
for line in f:
	print "Getting running-config " + (line)
	HOST = line.strip()
	tn = telnetlib.Telnet(HOST)

	tn.read_until("Username: ")
	tn.write(user + "\n")
	if password:
	    tn.read_until("Password: ")
	    tn.write(password + "\n")

	tn.write("terminal length 0\n")
	tn.write("show run\n")
	tn.write("exit\n")
	print('Exiting the switch ' + str(HOST) + ' after taking the Backup \n')
        
	readoutput = tn.read_all()
        saveoutput =  open("Router_CFG_BKUP_" + HOST, "w")
        saveoutput.write(readoutput)
        saveoutput.write("\n")
	saveoutput.close()
