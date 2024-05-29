from netmiko import ConnectHandler
import getpass
import sys

# passw = getpass.getpass('Password: ')
# secr = getpass.getpass('Secret: ')
passw = "wenkel"
secr = "hej"

gateway = ConnectHandler (device_type = 'cisco_ios', ip = str (sys.argv [1]), username = str (sys.argv [2]), password = passw, secret = secr)
gateway.enable()

gateway_commands = [
	"hostname Gateway",
	"int se0/0/0",
	"ip addr 192.168.1.1 255.255.255.0",
	"clockrate 64000",
	"no shut",
	"exit",
	"ip route 0.0.0.0 0.0.0.0 192.168.1.2",
	"int g0/0",
	"no shut",
	"exit",
	"int g0/0.1",
	"description Management VLAN 1",
	"encapsulation dot1q 1 native",
	"ip addr 172.16.1.1 255.255.255.0",
	"exit",
	"int g0/0.100",
	"description Payroll VLAN 100",
	"encapsulation dot1q 100",
	"ip addr 172.16.100.1 255.255.255.0",
	"exit",
	"int g0/0.200",
	"description Engineering VLAN 200",
	"encapsulation dot1q 200",
	"ip addr 172.16.200.1 255.255.255.0",
	"exit",
	"int g0/0.99",
	"encapsulation dot1q 99",
	"ip addr 172.17.99.3 255.255.255.0",
	"exit"
	]

gateway.send_config_set (gateway_commands)
gateway.disconnect ()
