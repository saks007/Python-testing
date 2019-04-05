import paramiko, getpass, time

devices = {"iosv-1": {"ip": "192.168.1.1"}, "iosv-2": {"ip": "192.168.1.3"}}
commands = ["show version\n", "show run\n"]

# username = input('Username: ')
# password = getpass.getpass('Password: ')

max_buffer = 65535


def clear_buffer(connection):
    if connection.recv_ready():
        return connection.recv(max_buffer)


# Starts the loop for devices
for device in devices.keys():
    outputFileName = device + "_output.txt"
    connection = paramiko.SSHClient()
    connection.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    connection.connect(
        devices[device]["ip"],
        username=cisco,
        password=cisco,
        look_for_keys=False,
        allow_agent=False,
    )
    new_connection = connection.invoke_shell()
    output = clear_buffer(new_connection)
    time.sleep(2)
    new_connection.send("terminal length 0\n")
    output = clear_buffer(new_connection)
    with open(outputFileName, "wb") as f:
        for command in commands:
            new_connection.send(command)
            time.sleep(2)
            output = new_connection.recv(max_buffer)
            print(output)
            f.write(output)

    new_connection.close()
