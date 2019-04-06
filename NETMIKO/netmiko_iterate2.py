from netmiko import ConnectHandler

with open('commands') as f:
    command_to_send = f.read().splitlines()

 cisco = {
    'device_type': 'cisco_ios',
    'host':   '192.168.1.1',
    'username': 'cisco',
    'password': 'cisco',
}

All_devices = [cisco]

for device in All_devices:
    net_connect = ConnectHandler(**device)
    output = net_connect.send_config_set(command_to_send)
    print(output)