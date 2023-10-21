#!/bin/bash

# Function to show a pulsating Zenity popup
show_pulsating_popup() {
  (zenity --progress --window-icon="info" --text=$1 --title="Capsule audio profile" --pulsate --width=400 --timeout=3) &
  pulsate_pid=$!
}

profile_address="84_AC_60_10_E4_DE"

if pacmd list-cards | grep -q -e "active profile: <a2dp_sink>"; then
    show_pulsating_popup "A2DP->Handsfree"
    pacmd set-card-profile bluez_card.$profile_address handsfree_head_unit
else
    show_pulsating_popup "Handsfree->A2DP"
    pacmd set-card-profile bluez_card.$profile_address a2dp_sink
fi

exit 0

