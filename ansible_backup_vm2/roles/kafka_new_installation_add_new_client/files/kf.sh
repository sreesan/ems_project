

#!/bin/bash

cd /opt/ems/kafka/kafka_2.12-0.11.0.1
bin/kafka-server-start.sh -daemon config/server.properties
