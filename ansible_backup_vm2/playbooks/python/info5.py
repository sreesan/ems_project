


#!/usr/bin/env python
#import platform, subprocess, re
import sys
import os
import socket

print ('The Ip adddress of server is:' '\n')
print socket.gethostbyname(socket.gethostname())
print ("The hostname of server is:" '\n')
print socket.gethostname()

system = os.uname()
print ("The information of system is:" '\n' , system)
print ("The os version is:" '\n')
osver = os.system("cat /etc/redhat-release")
print ("The status of memory is:" '\n')
space = os.system("free -m"
print ("The CPU status of server is:" '\n')
cpu = os.system("inxi -C")

