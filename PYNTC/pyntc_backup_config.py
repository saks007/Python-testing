from pyntc import ntc_device as NTC

iosvl2 = NTC(host='192.168.1.1', username='cisco', password='cisco', device_type='cisco_ios_ssh')
iosvl2.open()

config = iosvl2.running_config
print  'Backing up the running configuration from the switch..'

host = '192.168.1.1'
save_file = open ('Switch_' + host , 'w')
save_file.write(config)
save_file.close
