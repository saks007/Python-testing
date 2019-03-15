from netmiko import ConnectHandler
import netmiko 

cisco = {
    'device_type': 'cisco_ios',
    'host':   '192.168.1.1',
    'username': 'cisco',
    'password': 'cisco',
 }

net_connect = ConnectHandler(**cisco) 
net_connect.find_prompt()
output = net_connect.send_command("show ip int brief")
print(output)

