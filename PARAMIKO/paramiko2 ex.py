import paramiko, time

con = paramiko.SSHClient()
con.set_missing_host_key_policy(paramiko.AutoAddPolicy())
con.connect(
    "192.168.1.1",
    username="cisco",
    password="cisco",
    look_for_keys=False,
    allow_agent=False,
)
stdin, stdout, stderr = con.exec_command("show ver")
stdout.read()
