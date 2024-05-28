from netmiko import ConnectHandler
import getpass
import sys

# passw = getpass.getpass('Password: ')
# secr = getpass.getpass('Secret: ')
passw = "wenkel"
secr = "hej"

isp = ConnectHandler (device_type = 'cisco_ios', ip = str (sys.argv [1]), username = str (sys.argv [2]), password = passw, secret = secr)
isp.enable()

isp_commands = [
	"hostname ISP",
	"int lo0",
	"ip addr 200.200.200.1 255.255.255.0",
	"int se0/0/0",
	"ip addr 192.168.1.2 255.255.255.0",
	"no shut",
	"exit",
	"ip route 172.16.0.0 255.255.0.0 192.168.1.1"
	]

isp.send_config_set (isp_commands)
isp.disconnect ()
