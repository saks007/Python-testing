from pyntc import ntc_device as NTC

hostlist = ['192.168.1.1','192.168.1.2']

for i in hostlist:
    print 'Taking backup for switch : ' + str(i) + '\n'
    iosvl2 = NTC(host=i, username='cisco', password='cisco', device_type='cisco_ios_ssh')
    iosvl2.open()
    iosvl2.save()
    iosvl2.backup_running_config('Switch_' + str(i) + '.cfg')
    iosvl2.close