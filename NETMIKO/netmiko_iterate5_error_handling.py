
from netmiko import ConnectHandler
from getpass import getpass
from netmiko.ssh_exception import  AuthenticationException

with open('commands') as f:
    command_to_send = f.read().splitlines()

with open('ipaddress') as f:
    device_ip= f.read().splitlines()

for device in device_ip:
    username = raw_input('Enter username to login to Switch ' + str (device) + ' :')
    password = getpass()
    cisco = {
        'device_type': 'cisco_ios',
        'host':   device,
        'username': username,
        'password': password,
    }
    try:
        net_connect = ConnectHandler(**cisco)
    except (AuthenticationException):
        print 'Authentication Failure :' + device
        continue
    print 'Configuring switch ' + str(device)
    output = net_connect.send_config_set(command_to_send)
    print(output)
