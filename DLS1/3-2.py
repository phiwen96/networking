from netmiko import ConnectHandler
import getpass
import sys
import telnetlib
from telnetlib import Telnet

# passw = getpass.getpass('Password: ')
# secr = getpass.getpass('Secret: ')

passw = "wenkel"
secr = "hej"

# tel = telnetlib.Telnet(sys.argv [1], 23, timeout=6)
tel = telnetlib.Telnet(sys.argv [1])

tel.write (str (sys.argv [2]).encode ('ascii') + b"\n")
tel.write (passw.encode ('ascii') + b"\n")
# tel.write ("conf t".encode ('ascii') + b"\n")
tel.write (b"en\n")
tel.write (b"hej\n")
tel.write (b"sh run\n       ")
# tel.write (b"       \n")
tel.write (b"exit\n")
tel.write (b"exit\n")
# tel.write (b"exit\n")
print (tel.read_all ().decode ('ascii'))
# print (tel.read_all ().decode ('ascii'))
# tel = telnetlib.Telnet(sys.argv [1])
# tel.read_until(b"Username:")
# tel.write(sys.argv [2].encode('ascii') + b"\n")
# tel.read_until(b"Password:")
# tel.write(passw.encode('ascii') + b"\n")

# tel.write(b"show version\n")

# tel.write(b"exit\n")
# print(tel.read_all().decode('ascii'))

# dls1_commands = [
# 	"spanning-tree vlan 1 root primary", 
# 	"int range fa0/7-12",
# 	"switchport trunk encapsulation dot1q",
# 	"switchport mode trunk"]

# dls1.send_config_set (dls1_commands)
# dls1.disconnect ()
