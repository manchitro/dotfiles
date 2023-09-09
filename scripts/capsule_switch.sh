#!/bin/bash

# Bluetooth device address (replace with your device's address)
device_address="84:AC:60:10:E4:DE"

# Function to show a Zenity progress dialog
show_progress() {
    (
        echo "10"
        echo "# Performing Bluetooth operation..."
        
        # Check if the device is currently connected
        connected=$(bluetoothctl info $device_address | grep "Connected: yes")

        if [ -n "$connected" ]; then
            # If connected, disconnect
            bluetoothctl <<EOF
            disconnect $device_address
            exit
EOF
            echo "50"
            echo "# Disconnecting..."
        else
            # If not connected, connect
            bluetoothctl <<EOF
            connect $device_address
            exit
EOF
            echo "50"
            echo "# Connecting..."
        fi

        sleep 2
        echo "100"
    ) | zenity --progress --pulsate --auto-close --width=400 --title="Capsule On/Off"
}

# Show the progress dialog
show_progress &

exit 0
