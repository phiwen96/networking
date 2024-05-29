from netmiko import ConnectHandler
import getpass
import sys

passw = getpass.getpass('Password: ')
secr = getpass.getpass('Secret: ')

dls1 = ConnectHandler (device_type = 'cisco_ios', ip = str (sys.argv [1]), username = str (sys.argv [2]), password = passw, secret = secr)
dls1.enable()

dls1_commands = [
	"hostname DLS1",
	"vtp mode server",
	"vtp domain CISCO",
	"vlan 10",
	"name Red",
	"exit",
	"vlan 20",
	"name Blue",
	"exit",
	"vlan 30",
	"name Orange",
	"exit",
	"vlan 40",
	"name Green",
	"exit",
	"spanning-tree vlan 10 root primary",
	"spanning-tree vlan 20 root primary",
	"spanning-tree vlan 30 root primary",
	"spanning-tree vlan 40 root primary",
	"int fa0/12",
	"no switchport",
	"ip addr 172.16.11.1 255.255.255.0",
	"no shut",
	"exit",
	"int lo0",
	"ip addr 172.16.1.1 255.255.255.0",
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
	"int range fa0/7-8",
	"channel-group 1 mode desirable",
	"exit",
	"int range fa0/9-10",
	"channel-group 2 mode desirable",
	"exit",





	"int vlan 1",
	"ip addr 172.16.1.1 255.255.255.0",
	"no shut",
	"exit",
	"ip default-gateway 172.16.1.1",
	"int range fa0/7-8",
	"switchport trunk encapsulation dot1q",
	"switchport mode trunk",
	"channel-group 1 mode desirable",
	"spanning-tree portfast trunk",
	"exit",
	"int range fa0/9-10",
	"switchport trunk encapsulation dot1q",
	"switchport mode trunk",
	"channel-group 2 mode desirable",
	"spanning-tree portfast trunk",
	"exit",
	"vtp domain SWPOD",
	"vtp version 2",
	"vlan 100",
	"name Finance",
	"vlan 200",
	"name Engineering",
	"exit",
	"int vlan 100",
	"ip addr 172.16.100.1 255.255.255.0",
	"no shut",
	"exit",
	"int vlan 200",
	"ip addr 172.16.200.1 255.255.255.0",
	"no shut",
	"exit",
	"ip routing"
	]

dls1.send_config_set (dls1_commands)
dls1.disconnect ()
