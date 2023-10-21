#!/bin/bash

# Function to show a pulsating Zenity popup
show_pulsating_popup() {
  (zenity --progress --window-icon="info" --text=$1 --title="Capsule connections" --pulsate --width=400 --timeout=3) &
  pulsate_pid=$!
}

# Bluetooth device address (replace with your device's address)
device_address="84:AC:60:10:E4:DE"
if bluetoothctl info $device_address | grep "Connected: yes"; then
    show_pulsating_popup "Disconnecting..."
    bluetoothctl disconnect $device_address
else
    show_pulsating_popup "Connecting..."
    bluetoothctl connect $device_address
fi

exit 0
