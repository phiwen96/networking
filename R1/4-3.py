from netmiko import ConnectHandler
import getpass
import sys

# passw = getpass.getpass('Password: ')
# secr = getpass.getpass('Secret: ')
passw = "wenkel"
secr = "hej"

R1 = ConnectHandler (device_type = 'cisco_ios', ip = str (sys.argv [1]), username = str (sys.argv [2]), password = passw, secret = secr)
R1.enable()

R1_commands = [
	"hostname R1",
	"int g0/1",
	"no shut",
	"exit",
	"int g0/1.10",
	"description Red VLAN 10",
	"encapsulation dot1q 10",
	"ip addr 172.16.10.2 255.255.255.0",
	"exit",
	"int g0/1.40",
	"description Green VLAN 40",
	"encapsulation dot1q 40",
	"ip addr 172.16.40.2 255.255.255.0",
	"exit",
	"router eigrp 1",
	"no auto-summary"
	"network 172.16.10.2 0.0.0.255",
	"network 172.16.40.2 0.0.0.255"
	]

R1.send_config_set (R1_commands)
R1.disconnect ()
