#!/usr/bin/env bash

#rm /var/lib/kafka/data/* -rf
gnome-terminal --tab --title "Zookeeper" -- bash -c "cd /opt/kafka/ && sudo bin/zookeeper-server-start.sh config/zookeeper.properties; bash";
sleep 3;
for i in 1 2 3
do
	gnome-terminal --tab --title "Broker $i" -- bash -c "cd /opt/kafka/ && sudo bin/kafka-server-start.sh config/server-$i.properties; bash";
	sleep 3;
done
exit 0;
