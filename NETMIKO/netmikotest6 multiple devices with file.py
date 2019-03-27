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

with open('router_config') as f:
    lines = f.read().splitlines()
print lines

for devices in all_devices:
    net_connect = ConnectHandler(**devices)
    output = net_connect.send_config_set(lines)
print output 
