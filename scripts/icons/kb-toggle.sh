#!/bin/bash

# Your custom icon path
ICON_PATH="/path/to/your/custom/icon.png"

# Function to show notification
show_notification() {
    notify-send "Custom Tray Icon" "You pressed the custom tray icon!"
}

# Create a simple system tray icon
create_tray_icon() {
    kdialog --passivepopup "Custom Tray Icon Script Running" 5
    while true; do
        choice=$(kdialog --menu "Custom Tray Icon Menu" \
            "Show Notification":1 \
            "Exit":2)
        
        case $choice in
            1) show_notification ;;
            2) exit ;;
        esac
    done
}

# Main entry point
create_tray_icon





# #!/bin/bash
# # Get the keyboard ID
# ID=$(xinput -list | grep -i 'AT Translated Set 2 keyboard' | awk '{print $7}' | cut -d '=' -f 2)
# # Get the keyboard status
# STATUS=$(xinput -list-props $ID | grep -i 'Device Enabled' | awk '{print $4}')
# # Toggle the keyboard status
# if [ $STATUS -eq 1 ]; then
#   xinput disable $ID
# else
#   xinput enable $ID
# fi



# #!/bin/bash

# show_pulsating_popup() {
#   (zenity --progress --window-icon="info" --text=$1 --title="ProtonVPN" --pulsate --width=400) &
#   pulsate_pid=$!
# }

# if protonvpn-cli status | grep -q 'Country'; then
#   show_pulsating_popup "Disconnecting..."
#   protonvpn-cli disconnect
#   kill -KILL $pulsate_pid
# else
#   show_pulsating_popup "Reconnecting..."
#   protonvpn-cli reconnect
#   kill -KILL $pulsate_pid
# fi

# exit 0
