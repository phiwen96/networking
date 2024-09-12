from net import *
from netmiko import ConnectHandler
import getpass
import sys



als1 = ConnectHandler (device_type = 'cisco_ios', ip = str (sys.argv [1]), username = str (sys.argv [2]), password = passw, secret = secr)
als1.enable()

als1_commands = [
	"spanning-tree vlan 1 root secondary", 
	"int range fa0/7-12", 
	"switchport mode trunk", 
	"int fa0/6", 
	"switchport mode access", 
	"spanning-tree portfast"]

als1.send_config_set (als1_commands)
als1.disconnect ()


def run (username, ip_DLS1, ip_DLS2, ip_ALS1, ip_ALS2):
	password = getpass.getpass('Password: ')
	secret = getpass.getpass('Secret: ')
	ALS1 = get_net_device (ip_ALS1, username, password, secret)
	ALS2 = get_net_device (ip_ALS2, username, password, secret)
	DLS1 = get_net_device (ip_DLS1, username, password, secret)
	DLS2 = get_net_device (ip_DLS2, username, password, secret)
