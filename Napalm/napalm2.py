import json
from napalm import get_network_driver

driver = get_network_driver("ios")
iosvl2 = driver("192.168.1.1", "cisco", "cisco")
iosvl2.open()

# ios_output = iosvl2.get_facts()
# print (json.dumps(ios_output, indent=2))


# ios_output = iosvl2.get_arp_table()
# print (json.dumps(ios_output, indent=2))

ios_output = iosvl2.get_mac_address_table()
print(json.dumps(ios_output, indent=5))

ios_output = iosvl2.get_arp_table()
print(json.dumps(ios_output, indent=2))

ios_output = iosvl2.ping("192.168.1.10")
print(json.dumps(ios_output, indent=2))
