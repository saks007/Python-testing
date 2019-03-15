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

commands=['hostname xcxc', 'end', 'wri']
output = net_connect.send_config_set(commands)
print output
#net_connect.save_config()
net_connect.disconnect()
