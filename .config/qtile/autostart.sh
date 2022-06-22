#!/bin/sh

light-locker --lock-on-lid --lock-on-suspend &
picom -b &
guake &
nm-applet &
xcape -e 'Super_L=Alt_L|F1' &
bash /home/s/scripts/ofc.sh &
nitrogen --restore --set-zoom-fill &
greenclip daemon &
keynav &
transmission-gtk -m &
blueman-applet &
kdeconnect-cli -l &
protonvpn &