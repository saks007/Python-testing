import pexpect

devices = {"R1": {"prompt": "R1", "ip": "192.168.2.20"}}

un = "cisco"
pw = "cisco"

print(devices["R1"]["ip"])

child = pexpect.spawn("telnet " + devices["R1"]["ip"])
child.expect("Username")
child.sendline(un)
child.expect("Password")
child.sendline(pw)
child.expect(devices["R1"]["prompt"])
child.sendline("sh ver")
child.expect(devices["R1"]["prompt"])
print(child.before)
child.sendline("exit")
