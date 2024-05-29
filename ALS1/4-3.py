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




	"int vlan 1",
	"ip addr 172.16.1.101 255.255.255.0",
	"no shut",
	"exit",
	"ip default-gateway 172.16.1.1",
	"int range fa0/11-12",
	"switchport mode trunk",
	"channel-group 1 mode desirable",
	"spanning-tree portfast trunk",
	"exit",
	"int range fa0/7-8",
	"switchport mode trunk",
	"channel-group 2 mode desirable",
	"spanning-tree portfast trunk",
	"exit",
	"vtp mode client",
	"int fa0/6",
	"switchport mode access",
	"switchport access vlan 100",
	"spanning-tree portfast",
	"exit",
	]

ALS1.send_config_set (ALS1_commands)
ALS1.disconnect ()
