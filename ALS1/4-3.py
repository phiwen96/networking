from netmiko import ConnectHandler
import getpass
import sys

# passw = getpass.getpass('Password: ')
# secr = getpass.getpass('Secret: ')
passw = "wenkel"
secr = "hej"

ALS1 = ConnectHandler (device_type = 'cisco_ios', ip = str (sys.argv [1]), username = str (sys.argv [2]), password = passw, secret = secr)
ALS1.enable()

ALS1_commands = [
	"hostname ALS1",
	"int range fa0/11-12",
	"shut",
	"exit",
	"vtp mode client",
	"vtp domain CISCO",
	"int range fa0/7-10",
	"switchport mode trunk",
	"spanning-tree portfast trunk",
	"no shut",
	"exit",
	"int range fa0/7-8",
	"channel-group 1 mode desirable",
	"exit",
	"int range fa0/15-17",
	"switchport mode access",
	"switchport access vlan 10",
	"spanning-tree portfast",
	"no shut",
	"exit",
	"int range fa0/18-19",
	"switchport mode access",
	"switchport access vlan 20",
	"spanning-tree portfast",
	"no shut",
	"exit",
	"int fa0/20",
	"switchport mode access",
	"switchport access vlan 30",
	"spanning-tree portfast",
	"no shut",
	"exit",
	"int vlan 30",
	"ip addr 172.16.30.1 255.255.255.0",
	"no shut",
	"exit",
	]

ALS1.send_config_set (ALS1_commands)
ALS1.disconnect ()
