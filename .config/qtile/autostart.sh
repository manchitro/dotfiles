#!/bin/sh

light-locker --lock-on-lid --lock-on-suspend &
dunst &
picom -b &
guake &
nm-applet &
xcape -e 'Super_L=Alt_L|F1' &
nitrogen --restore --set-zoom-fill &
greenclip daemon &
keynav &
transmission-gtk -m &
blueman-applet &
kdeconnect-cli -l &
protonvpn &
xbacklight -set 70 &
sh /home/s/scripts/generate_installed_list.sh &
sudo isw -b on
