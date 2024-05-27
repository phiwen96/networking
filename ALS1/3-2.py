from netmiko import ConnectHandler
import getpass
import sys

passw = getpass.getpass('Password: ')
secr = getpass.getpass('Secret: ')

als1 = ConnectHandler (device_type = 'cisco_ios', ip = str (sys.argv [1]), username = str (sys.argv [2]), password = passw, secret = secr)
als1.enable()

als1_commands = [
	"spanning-tree vlan 1 root secondary", 
	"int range fa0/7-12", 
	"switchport mode trunk", 
	"int fa0/6", 
	"switchport mode access", 
	"spanning-tree portfast"]

als1.send_config_set (als1_commands)
als1.disconnect ()
