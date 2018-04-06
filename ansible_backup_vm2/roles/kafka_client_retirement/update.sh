#!/bin/bash
ansible-playbook /etc/ansible/kafka_update_afterretirement.yml -i /etc/ansible/roles/kafka_installation/environments/in01-kafka-servers/hosts.ini


