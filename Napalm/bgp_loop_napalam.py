import json
from napalm import get_network_driver

bgplist = {"192.168.1.1", "192.168.1.2"}

for ip_address in bgplist:
    print "Displaying BGP Neighbour details on switch:" + str(ip_address) + "\n"
    driver = get_network_driver("ios")
    iosvl2 = driver(ip_address, "cisco", "cisco")
    iosvl2.open()
    ios_output = iosvl2.get_bgp_neighbors()
    print (json.dumps(ios_output, indent=4))
    iosvl2.close()
