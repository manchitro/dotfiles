#!/bin/bash

/home/s/orion/eap7-web/bin/standalone.sh &
sleep 1;
xdotool key alt+shift+j
for run in {1..9}; do xdotool key control+alt+shift+k; done

return 1;
