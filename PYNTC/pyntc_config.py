from pyntc import ntc_device as NTC

iosvl2 = NTC(host='192.168.1.1', username='cisco', password='cisco', device_type='cisco_ios_ssh')
iosvl2.open()

# single command configuration
iosvl2.config('hostname Switch1')

# multiple commands configurations
iosvl2.config_list(['hostname Sw1','int lo 10','ip add 20.20.20.1 255.255.255.0 '])
