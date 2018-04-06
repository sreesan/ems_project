


#!/usr/bin/env python
#import platform, subprocess, re
import sys
import os
import socket
import subprocess

print(' ')
print 'The Hostname Of Server is:' ,  socket.gethostname(),
#print ('The IP Adddress Of Server is:') , socket.gethostbyname(socket.gethostname()) ,
#print 'The Hostname Of Server is:' ,  socket.gethostname(),
system = os.uname()
print 'The Information Of System is:' , system,
p = subprocess.Popen("cat /etc/issue", stdout=subprocess.PIPE, shell=True)
(output , err) = p.communicate()
print ('The Version Of Operating System is:'  , output),
kernel = subprocess.Popen("uname -r", stdout=subprocess.PIPE, shell=True)
(output , err) = kernel.communicate()
print ('The Kernel Version Of Server is:' , output) ,
cpu = subprocess.Popen("cat /proc/cpuinfo", stdout=subprocess.PIPE, shell=True)
(output , err) = cpu.communicate()
print ('The Status Of CPU is:' , output) ,

mem = subprocess.Popen("free -m", stdout=subprocess.PIPE, shell=True)
(output , err) = mem.communicate()
print "The information of memory is: " , output

#print 'The Status Of Memory is:'
#space = os.system("free -m")

