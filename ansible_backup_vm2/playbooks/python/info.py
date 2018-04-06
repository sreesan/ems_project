


#!/bin/python
import socket
import os 
import sys
import platform
import psutil
import uuid

print  "Name: " +socket.gethostname() 
print "FQDN: " +socket.getfqdn()
print "System Platform: "+sys.platform
print "Machine: " +platform.machine()
print "Node " +platform.node()
print "Platform: "+platform.platform()
print "Pocessor: " +platform.processor()
print "System OS: "+platform.system()
print "Release: " +platform.release()
print "Version: " +platform.version()
print "Number of CPUs: " +str(psutil.cpu_count()) 
print "Number of Physical CPUs: " +str(psutil.cpu_count(logical=False))
