



#!/usr/bin/env python
#import platform, subprocess, re
import sys
import os
import socket

print(' ')
print ('The IP Adddress Of Server is:') , socket.gethostbyname(socket.gethostname())
print(' ')
print "The Hostname Of Server is:" ,  socket.gethostname()
print(' ')
system = os.uname()
print "The Information Of System is:" , system
print(' ')
print ("The os version is:")
osver = os.system("cat /etc/redhat-release")
print(' ')
print "The Status Of Memory is:"
space = os.system("free -m")
print(' ')
print "The CPU Status Of Server is:"
cpu = os.system("inxi -C")

