from netmiko import ConnectHandler
import getpass
import sys

passw = getpass.getpass('Password: ')
secr = getpass.getpass('Secret: ')

dls2 = ConnectHandler (device_type = 'cisco_ios', ip = str (sys.argv [1]), username = str (sys.argv [2]), password = passw, secret = secr)
dls2.enable()

dls2_commands = [
	"hostname DLS2",
	"vtp mode client",
	"vtp domain CISCO",
	"spanning-tree vlan 10 root secondary",
	"spanning-tree vlan 20 root secondary",
	"spanning-tree vlan 30 root secondary",
	"spanning-tree vlan 40 root secondary",
	"int fa0/12",
	"no switchport",
	"ip addr 172.16.11.2 255.255.255.0",
	"no shut",
	"exit",
	"int fa0/11",
	"switchport trunk encapsulation dot1q",
	"switchport mode trunk",
	"spanning-tree portfast trunk",
	"no shut",
	"exit",
	"int range fa0/7-10",
	"switchport trunk encapsulation dot1q",
	"switchport mode trunk",
	"spanning-tree portfast trunk",
	"no shut",
	"exit",
	"int vlan 10",
	"ip addr 172.16.10.1 255.255.255.0",
	"no shut",
	"exit"]

dls2.send_config_set (dls2_commands)
dls2.disconnect ()
