import getpass
import sys
import telnetlib
from telnetlib import Telnet
import telnetlib3

# passw = getpass.getpass('Password: ')
# secr = getpass.getpass('Secret: ')

passw = "wenkel"
secr = "hej"

dls1 = telnetlib.Telnet(sys.argv [1])

dls1.write (str (sys.argv [2]).encode ('ascii') + b"\n" + passw.encode ('ascii') + b"\nen\nhej\nconf t\n")
commands = b"""spanning-tree mode rapid-pvst
vtp mode transparent
vtp domain CISCO
vlan 10,20
spanning-tree vlan 10 priority 4096
int range g0/7-12
switchport trunk encapsulation dot1q
switchport mode trunk
no shut
"""

dls1.write (commands)
dls1.write (b"end\nexit\nexit\n")

print (dls1.read_all ().decode ('ascii'))