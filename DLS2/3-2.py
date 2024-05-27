from netmiko import ConnectHandler
import getpass
import sys

passw = getpass.getpass('Password: ')
secr = getpass.getpass('Secret: ')

dls2 = ConnectHandler (device_type = 'cisco_ios', ip = str (sys.argv [1]), username = str (sys.argv [2]), password = passw, secret = secr)
dls2.enable()

dls2_commands = [
	"spanning-tree vlan 1 root primary", 
	"int range fa0/7-12",
	"switchport trunk encapsulation dot1q",
	"switchport mode trunk"]

dls2.send_config_set (dls2_commands)
dls2.disconnect ()
