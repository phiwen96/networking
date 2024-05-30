from netmiko import ConnectHandler
import getpass
import sys

# passw = getpass.getpass('Password: ')
# secr = getpass.getpass('Secret: ')
passw = "wenkel"
secr = "hej"

ALS2 = ConnectHandler (device_type = 'cisco_ios', ip = str (sys.argv [1]), username = str (sys.argv [2]), password = passw, secret = secr)
ALS2.enable()

ALS2_commands = [
	"hostname ALS2",
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
	"int range fa0/9-10",
	"channel-group 2 mode desirable",
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
	"int vlan 40",
	"ip addr 172.16.20.1 255.255.255.0",
	"no shut",
	"exit",
	]

ALS2.send_config_set (ALS2_commands)
ALS2.disconnect ()
