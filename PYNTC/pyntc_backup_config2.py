from pyntc import ntc_device as NTC

iosvl2 = NTC(
    host="192.168.1.1", username="cisco", password="cisco", device_type="cisco_ios_ssh"
)
iosvl2.open()
iosvl2.backup_running_config("switch1.cfg")
