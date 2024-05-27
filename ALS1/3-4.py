from netmiko import ConnectHandler
import getpass
import sys

passw = getpass.getpass('Password: ')
secr = getpass.getpass('Secret: ')

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



# nr_gig_interfaces = 0
# nr_fa_interfaces = 0
# for item in als1_config:
#     if "interface FastEthernet" in item:
#         nr_fa_interfaces += 1
#         als1_commands.append (item)
#         als1_commands.append ('shut')
#     elif "interface GigabitEthernet" in item:
#         nr_fa_interfaces += 1
#         als1_commands.append (item)
#         als1_commands.append ('shut')



#config_commands = ["no ip domain-lookup", ]

#print (outp)

#x = 78

#for item in output:
#        if "interface Loopback" in item:
#            loopback_number = item [18:]
#            config_commands = ["interface Loopback" + str (loopback_number), 'ip address 30.30.30.' + str (x) + ' 255.255.255.255']
#            device.send_config_set (config_commands)
#            x += 1

#device.disconnect ()


# import telnetlib

#host = "10.1.1.1"
#user = "admin"
#password = "test"

#tel = telnetlib.Telnet(host, 23, timeout=2)

#tel.read_until(b"Username:")
#tel.write(user.encode('ascii') + b"\n")
#tel.read_until(b"Password:")
#tel.write(password.encode('ascii') + b"\n")

#tel.write(b"show version\n")

#tel.write(b"exit\n")
#print(tel.read_all().decode('ascii'))
# if len (sys.argv) != 6:
#         print ("usage: ptyhon ph.py ALS1 username")
#         exit(-1)
#ip_addr = str (sys.argv [1])
#user = str (sys.argv [2])