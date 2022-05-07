#!/usr/bin/env bash

#rm /var/lib/kafka/data/* -rf
/opt/kafka/bin/kafka-server-stop.sh /opt/kafka/config/server-1.properties;
sleep 8;
/opt/kafka/bin/zookeeper-server-stop.sh /opt/kafka/config/zookeeper.properties;
exit 0;
