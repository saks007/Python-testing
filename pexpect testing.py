import pexpect

child=pexpect.spawn('telnet 192.168.2.20')
child.expect('Username')
child.sendline('cisco')
child.expect('Password')
child.sendline('cisco')
child.expect('R1')
child.sendline('sh ver')
child.expect('R1')
print(child.before)
child.sendline('exit')
