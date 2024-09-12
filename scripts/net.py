from netmiko import ConnectHandler
import getpass
import sys

def get_net_device(ip, user, password, secret):
	dev = ConnectHandler (device_type = 'cisco_ios', ip = ip, username = user, password = password, secret = secret)
	dev.enable()
	return dev

def close_net_device(device):
	device.disconnect ()

