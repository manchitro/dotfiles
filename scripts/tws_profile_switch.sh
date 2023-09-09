#!/bin/bash

# Bluetooth device address (replace with your device's address)
device_address="84:AC:60:10:E4:DE"
profile_address="84_AC_60_10_E4_DE"

# Function to show a Zenity progress dialog
show_progress() {
    (
        echo "10"
        echo "# Switching Profile..."

        # Check if the device is currently connected
        connected=$(bluetoothctl info $device_address | grep "Connected: yes")

        if [ -n "$connected" ]; then
            # If connected, switch profiles
            pacmd list-cards | grep -q -e "active profile: <a2dp_sink>"
            if [ $? -eq 0 ]; then
                # Switch to handsfree_head_unit profile
                pacmd set-card-profile bluez_card.$profile_address handsfree_head_unit
                echo "Switched to handsfree_head_unit"
            else
                # Switch to a2dp_sink profile
                pacmd set-card-profile bluez_card.$profile_address a2dp_sink
                echo "Switched to a2dp_sink"
            fi
        else
            echo "Device is not connected. Please connect first."
        fi


        sleep 2
        echo "100"
    ) | zenity --progress --pulsate --auto-close --width=400 --title="Capsule Profile Switch"
}


# Show the progress dialog
show_progress &

exit 0

