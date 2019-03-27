import json
from napalm import get_network_driver

bgplist = {'192.168.1.1', '192.168.1.2'}

for ip_address in bgplist:
    print "Accessing switch:" + str(ip_address) + "\n"
    driver = get_network_driver('ios')
    iosvl2 = driver(ip_address, 'cisco', 'cisco')
    iosvl2.open()
    iosvl2.load_merge_candidate(filename='ACL1.cfg')
    iosvl2.commit_config()
    iosvl2.close()
