from netmiko import ConnectHandler

with open("commands") as f:
    command_to_send = f.read().splitlines()

with open("ipaddress") as f:
    device_ip = f.read().splitlines()

for device in device_ip:
    print "Configuring switch " + str(device)
    cisco = {
        "device_type": "cisco_ios",
        "host": device,
        "username": "cisco",
        "password": "cisco",
    }
    net_connect = ConnectHandler(**cisco)
    output = net_connect.send_config_set(command_to_send)
    print (output)
