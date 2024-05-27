from netmiko import ConnectHandler
import getpass
import sys

passw = getpass.getpass('Password: ')
secr = getpass.getpass('Secret: ')

als2 = ConnectHandler (device_type = 'cisco_ios', ip = str (sys.argv [1]), username = str (sys.argv [2]), password = passw, secret = secr)
als2.enable()

als2_commands = [
	"spanning-tree mode rapid-pvst",
	"vtp mode transparent",
	"vtp domain CISCO",
	"vlan 10,20",
	"exit",
	"int range fa0/7-12", 
	"switchport mode trunk",
	"no shut"]

als2.send_config_set (als2_commands)
als2.disconnect ()
