import json
from napalm import get_network_driver

driver = get_network_driver("ios")
iosvl2_sw1 = driver("192.168.1.1", "cisco", "cisco")
iosvl2_sw1.open()


driver = get_network_driver("ios")
iosvl2_sw2 = driver("192.168.1.2", "cisco", "cisco")
iosvl2_sw2.open()


ios_output = iosvl2_sw1.get_bgp_neighbors()
print(json.dumps(ios_output, indent=4))

iosvl2_sw1.close()

ios_output = iosvl2_sw2.get_bgp_neighbors()
print(json.dumps(ios_output, indent=4))

iosvl2_sw2.close()
