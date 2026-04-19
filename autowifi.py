import json
import netmiko
from netmiko import ConnectHandler

# WRITE, CONNECT, PUSH

### WRITE
# WRITE device information and configurations

# Read json file containing aironet settings
with open('autoAP-temp.json') as file:
    deviceData = json.load(file)

# parse info from json file
aironet = deviceData['aironetInfo']
apConfig = deviceData['aironetConfig']

# Write the script for the device
deviceConfig = [
    f'hostname {apConfig["hostname"]}',
    f'dot11 ssid {apConfig["ssid"]}',
    f'vlan {apConfig["vlan"]}',
    f'authentication {apConfig["authentication"]}',
    f'authentication key-management {apConfig["key-man"]}',
    f'wpa-psk ascii {apConfig["wifi-pass"]}',
    'guest-mode',
    'default Int Dot11Radio 0',
    'default interface gigabitEthernet 0',
    'int dot11radio 0',
    'no shut',
    f'channel {apConfig["channel"]}',
    f'encryption mode ciphers {apConfig["encr-mod"]}',
    f'encryption vlan {apConfig["vlan"]} mode ciphers {apConfig["encr-mod"]}',
    f'ssid {apConfig["ssid"]}',
    'exit',
    f'interface dot11radio 0.{apConfig["vlan"]}',
    f'encapsulation dot1q {apConfig["vlan"]} native',
    'bridge-group 1',
    'exit'
]

### CONNECT
# Connect to the device's CLI
accessAutoAP = ConnectHandler(**aironet)

# use enable command to enter privilege exec mode
accessAutoAP.enable()

### PUSH 
# Push configurations through global configuration mode
output = accessAutoAP.send_config_set(deviceConfig)

# Print CLI Output on the terminal
print(output)

# close connection
accessAutoAP.disconnect()



# create a show run output file
with open('show_run_output.txt', 'w') as file:
    file.write(output)