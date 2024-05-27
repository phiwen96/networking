from netmiko import ConnectHandler
import getpass
import sys

passw = getpass.getpass('Password: ')
secr = getpass.getpass('Secret: ')

dls2 = ConnectHandler (device_type = 'cisco_ios', ip = str (sys.argv [1]), username = str (sys.argv [2]), password = passw, secret = secr)
dls2.enable()

dls2_commands = [
	"vtp mode transparent",
	"vtp domain CISCO",
	"vlan 10,20,30,40,50,60,70,80,90,100",
	"int range fa0/7-12",
	"switchport trunk encapsulation dot1q",
	"switchport mode trunk",
	"no shut",
	"exit",
	"spanning-tree mode mst",
	"spanning-tree mst configuration",
	"name CISCO",
	"revision 1",
	"instance 1 vlan 20-50",
	"instance 2 vlan 80,100"]

dls2.send_config_set (dls2_commands)
dls2.disconnect ()
