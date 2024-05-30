#!/usr/bin/bash

# Touchpad config
kwriteconfig5 --file ~/.config/touchpadxlibinputrc --group "CUST0001:00 04F3:30AA Touchpad"  --key naturalScroll true
kwriteconfig5 --file ~/.config/touchpadxlibinputrc --group "CUST0001:00 04F3:30AA Touchpad"  --key clickMethodAreas false
kwriteconfig5 --file ~/.config/touchpadxlibinputrc --group "CUST0001:00 04F3:30AA Touchpad"  --key clickMethodClickfinger true
kwriteconfig5 --file ~/.config/touchpadxlibinputrc --group "CUST0001:00 04F3:30AA Touchpad"  --key pointerAcceleration 0.2
kwriteconfig5 --file ~/.config/touchpadxlibinputrc --group "CUST0001:00 04F3:30AA Touchpad"  --key tapToClick true
