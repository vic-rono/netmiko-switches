from netmiko import ConnectHandler

SW1 = {
  'device_type': 'cisco_ios',
  'ip': '192.168.122.72',
  'username': 'korir',
  'password': 'victorsecrets'
}


SW2 = {
  'device_type': 'cisco_ios',
  'ip': '192.168.122.82',
  'username': 'korir',
  'password': 'victorsecrets'
}

SW3 = {
  'device_type': 'cisco_ios',
  'ip': '192.168.122.83',
  'username': 'korir',
  'password': 'victorsecrets',
}

all_devices = [SW1, SW2, SW3]

for devices in all_devices:
    net_connect = ConnectHandler(**devices)
    for x in range(2,21):
      print("Create VLAN " + str(x))
      config_commands = ['vlan ' + str(x), 'name VLAN_ ' + str(x)]
      output = net_connect.send_config_set(config_commands)
      print (output)

