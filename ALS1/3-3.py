from netmiko import ConnectHandler
import getpass
import sys

# passw = getpass.getpass('Password: ')
# secr = getpass.getpass('Secret: ')
passw = "wenkel"
secr = "hej"

als1 = ConnectHandler (device_type = 'cisco_ios', ip = str (sys.argv [1]), username = str (sys.argv [2]), password = passw, secret = secr)
als1.enable()

als1_commands = [
	"spanning-tree mode rapid-pvst",
	"vtp mode transparent",
	"vtp domain CISCO",
	"vlan 10, 20",
	"int range fa0/7-12", 
	"switchport mode trunk",
	"no shut"]

als1.send_config_set (als1_commands)
als1.disconnect ()
