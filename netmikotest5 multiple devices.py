from netmiko import ConnectHandler

ios1 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.1.1',
    'username': 'cisco',
    'password': 'cisco',
}

ios2 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.1.3',
    'username': 'cisco',
    'password': 'cisco',
}

ios3 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.1.4',
    'username': 'cisco',
    'password': 'cisco',
}


all_devices = [ios1, ios2, ios3]

for devices in all_devices:
    net_connect = ConnectHandler(**devices)
    for n in range (13,14):
       print "Creating loopback interface " + str(n)
       config_commands = ['int lo' + str(n), 'ip add 120.20.20.'+str(n)+ ' 255.255.255.0']
       output = net_connect.send_config_set(config_commands)
print output 
