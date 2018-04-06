

#!/usr/bin/env python
#import platform, subprocess, re
import sys
import os
import socket
import subprocess

print(' ')
print 'The Hostname Of Server is:' ,  socket.gethostname(), 
print(','),
print ('The IP Adddress Of Server is:') , socket.gethostbyname(socket.gethostname()) ,
print(','),
#print 'The Hostname Of Server is:' ,  socket.gethostname(),
system = os.uname()
print 'The Information Of System is:' , system,
print(','),
p = subprocess.Popen("cat /etc/redhat-release", stdout=subprocess.PIPE, shell=True)
(output , err) = p.communicate()
print ('The Version Of Operating System is:'  , output), 
print(','),
kernel = subprocess.Popen("uname -r", stdout=subprocess.PIPE, shell=True)
(output , err) = kernel.communicate()
print ('The Kernel Version Of Server is:' , output) ,
print(','),
cpu = subprocess.Popen("inxi -C", stdout=subprocess.PIPE, shell=True)
(output , err) = cpu.communicate()
print ('The Status Of CPU is:' , output), 
print('')
#mem = subprocess.Popen("free -m", stdout=subprocess.PIPE, shell=True)
#(output , err) = mem.communicate()
#print "The information of memory is: " , output

#print 'The Status Of Memory is:'
#space = os.system("free -m")





