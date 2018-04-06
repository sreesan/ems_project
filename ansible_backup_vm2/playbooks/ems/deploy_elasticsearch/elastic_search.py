#!/usr/bin/env python
#import platform, subprocess, re
import sys
import os
import socket
import subprocess


#p = subprocess.Popen("yum update -y", stdout=subprocess.PIPE, shell=True)
#(output , err) = p.communicate()
#print (output)

p = subprocess.Popen("yum install java-1.8.0-openjdk.x86_64 -y", stdout=subprocess.PIPE, shell=True)
(output , err) = p.communicate()
print (output)

p=subprocess.Popen("yum install wget -y", stdout=subprocess.PIPE, shell=True)
(output , err) = p.communicate()
print (output)

p = subprocess.Popen("wget https://download.elastic.co/elasticsearch/elasticsearch/elasticsearch-1.7.3.noarch.rpm", stdout=subprocess.PIPE, shell=True)
(output , err) = p.communicate()
print (output)


p = subprocess.Popen("rpm -ivh elasticsearch-1.7.3.noarch.rpm", stdout=subprocess.PIPE, shell=True)
(output , err) = p.communicate()
print (output)

p = subprocess.Popen("systemctl enable elasticsearch.service", stdout=subprocess.PIPE, shell=True)
(output , err) = p.communicate()
print (output)



