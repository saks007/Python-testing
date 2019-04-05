import getpass
import sys
import telnetlib

HOST = "192.168.1.1"
user = raw_input("Enter your remote account: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until("Username: ")
tn.write(user + "\n")
if password:
    tn.read_until("Password: ")
    tn.write(password + "\n")


tn.write("conf t\n")

t = input("how many loopback interfaces would like to create:")
x = input("from which range:")
k = x + t

for i in range(x + 1, k + 1):

    tn.write("int lo" + str(i) + "\n")
    tn.write("ip add 10.10.10." + str(i) + " 255.255.255.0 \n")

tn.write("end\n")
tn.write("wri\n")

tn.write("exit\n")

print tn.read_all()
