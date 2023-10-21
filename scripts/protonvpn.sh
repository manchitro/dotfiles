#!/bin/bash

show_pulsating_popup() {
  (zenity --progress --window-icon="info" --text=$1 --title="ProtonVPN" --pulsate --width=400) &
  pulsate_pid=$!
}

if protonvpn-cli status | grep -q 'Country'; then
  show_pulsating_popup "Disconnecting..."
  protonvpn-cli disconnect
  kill -KILL $pulsate_pid
else
  show_pulsating_popup "Reconnecting..."
  protonvpn-cli reconnect
  kill -KILL $pulsate_pid
fi

exit 0
