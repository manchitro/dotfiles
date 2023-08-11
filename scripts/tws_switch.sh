#!/usr/bin/env bash

rfkill unblock bluetooth;
if bluetoothctl info 84:AC:60:10:E4:DE | grep -q "Connected: yes"; then
	bluetoothctl disconnect 84:AC:60:10:E4:DE;
else
	bluetoothctl connect 84:AC:60:10:E4:DE;
fi

exit 1;
