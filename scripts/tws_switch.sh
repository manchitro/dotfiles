#!/usr/bin/env bash

if bluetoothctl info FC:E8:06:16:0C:AA | grep -q "Connected: yes"; then
	bluetoothctl disconnect FC:E8:06:16:0C:AA;
else
	bluetoothctl connect FC:E8:06:16:0C:AA;
fi

exit 1;
