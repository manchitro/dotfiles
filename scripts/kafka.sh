#!/usr/bin/env bash

gnome-terminal --tab --title "Zookeeper" -- bash -c "/home/s/orion/kafka_2.13-2.8.0/bin/zookeeper-server-start.sh /home/s/orion/kafka_2.13-2.8.0/config/zookeeper.properties; bash";
sleep 3;
gnome-terminal --tab --title "Kafka" -- bash -c "/home/s/orion/kafka_2.13-2.8.0/bin/kafka-server-start.sh /home/s/orion/kafka_2.13-2.8.0/config/server.properties; bash";
exit 0;
