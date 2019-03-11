#!/usr/bin/env python3

from ncclient import manager

conn = manager.connect(
    host='sbx-nxos-mgmt.cisco.com',
    port=8181,
    username='admin',
    password='Admin_1234!',
    hostkey_verify=False,
    device_params={'name': 'nexus'},
    look_for_keys=False
)

for value in conn.server_capabilities:
    print(value)

conn.close_session()


