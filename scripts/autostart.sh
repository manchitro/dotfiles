#!/usr/bin/bash

notify-send "Executing autostart.sh" &
keynav &
syncthing serve --no-browser --logfile=default &
#picom --config ~/.config/picom/picom.conf --experimental-backends &
#sh .config/eww/ewwlaunch.sh
#nm-applet &
#teamviewer &
#xcape -e 'Super_L=Alt_L|F1' &
/usr/bin/bash -c "/usr/bin/xmodmap $HOME/.Xmodmap" &
#xinput set-button-map 17 1 2 8 4 5 6 7 3;
#unclutter -idle 3 -root & 
#feh --bg-fill /home/s/wallpapers/Sundarbans_web_cropped.jpg
#greenclip daemon &
#transmission-gtk &
#blueman-applet &
#pactl -- set-sink-volume @DEFAULT_SINK@ 70%
#sh /home/s/scripts/generate_installed_list.sh &
#sh /home/s/scripts/g304remap.sh &
#sudo isw -b on
#deadd-notification-center & disown
# flameshot &
#libinput-gestures-setup restart 
#touchpad-indicator & disown
#xdotool key F1 && sleep 1 && env DESKTOPINTEGRATION=no /opt/kuro/Kuro.AppImage --no-sandbox %U & disown
#xhost +si:localuser:ss
#gpaste-client &
#mpris-proxy &
#playerctld daemon &
#/usr/lib/kdeconnectd &
#kdeconnect-indicator &
#sleep 10
#alttab -fg "#CDD6F4" -bg "#1E1E2E" -frame "#89b4fa" -inact "#313244" -font xft:HackNerdFontComplete-Regular -t 500x50 -vertical -d 2 -mk Super_L -kk grave & alttab -fg "#CDD6F4" -bg "#1E1E2E" -frame "#89b4fa" -inact "#313244" -font xft:HackNerdFontComplete-Regular -t 500x50 -vertical -d 0 -bw 10 -bc "#1E1E2E" & disown
# sudo python3 /home/s/repo/MSI-Dragon-Center-for-Linux/set_fan.py 80 &
