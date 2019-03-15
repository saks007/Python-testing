import getpass
import time
import paramiko

	
user = raw_input("Enter your remote account: ")
password = getpass.getpass()

f = open('ipadd')
for l in f:
    print('configuring switch with ' + l +'\n')
    ssh_client = paramiko.SSHClient()
	ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	ssh_client.connect(hostname=l,username=user,password=password,look_for_keys=False,allow_agent=False)

	print "Successful connection", l

	remote_connection = ssh_client.invoke_shell()

	remote_connection.send("configure terminal\n")
	remote_connection.send("router ospf 1\n")
	remote_connection.send("network 0.0.0.0 255.255.255.255 area 0\n")

#for n in range (2,21):
#    print "Creating VLAN " + str(n)
#    remote_connection.send("vlan " + str(n) +  "\n")
#    remote_connection.send("name Python_VLAN " + str(n) +  "\n")
#    time.sleep(0.5)

	remote_connection.send("end\n")
	remote_connection.send("wri\n")
	remote_connection.send("exit\n")

	time.sleep(1)
	output = remote_connection.recv(65535)
	print output

