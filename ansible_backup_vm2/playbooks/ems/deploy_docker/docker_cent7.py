


#!/usr/bin/env python
#import platform, subprocess, re
import sys
import os
import socket
import subprocess

p = subprocess.Popen("yum install epel-release -y", stdout=subprocess.PIPE, shell=True)
(output , err) = p.communicate()
print (output)

p=subprocess.Popen("yum install docker -y", stdout=subprocess.PIPE, shell=True)
(output , err) = p.communicate()
print (output)

p = subprocess.Popen("yum install docker-io -y", stdout=subprocess.PIPE, shell=True)
(output , err) = p.communicate()
print (output)


p = subprocess.Popen("systemctl start docker", stdout=subprocess.PIPE, shell=True)
(output , err) = p.communicate()
print (output)







