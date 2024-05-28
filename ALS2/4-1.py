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
	"int vlan 1",
	"ip addr 172.16.1.102 255.255.255.0",
	"no shut",
	"exit",
	"ip default-gateway 172.16.1.1",
	"int range fa0/11-12",
	"switchport mode trunk",
	"channel-group 1 mode desirable",
	"exit",
	"vtp mode client",
	"int fa0/6",
	"switchport mode access",
	"switchport access vlan 200",
	"spanning-tree portfast",
	"exit"
	]

ALS2.send_config_set (ALS2_commands)
ALS2.disconnect ()
