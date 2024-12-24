#!/bin/bash

# Set Flameshot shortcuts using kwriteconfig5
kwriteconfig5 --file kglobalshortcutsrc --group org.flameshot.Flameshot.desktop --key "Capture" "Print,none,Take screenshot"
kwriteconfig5 --file kglobalshortcutsrc --group org.flameshot.Flameshot.desktop --key "Configure" "none,none,Configure"
kwriteconfig5 --file kglobalshortcutsrc --group org.flameshot.Flameshot.desktop --key "Launcher" "none,none,Open launcher"
kwriteconfig5 --file kglobalshortcutsrc --group org.flameshot.Flameshot.desktop --key "_k_friendly_name" "Flameshot"
kwriteconfig5 --file kglobalshortcutsrc --group org.flameshot.Flameshot.desktop --key "_launch" "none,none,Flameshot"
echo "Flameshot shortcuts have been configured."

# Configure Google Chrome shortcuts
kwriteconfig5 --file kglobalshortcutsrc --group google-chrome.desktop --key "_launch" "Meta+B,none,Launch Google Chrome"
kwriteconfig5 --file kglobalshortcutsrc --group chrome-uni.desktop --key "_launch" "Meta+Alt+B,none,Launch Google Chrome"
kwriteconfig5 --file kglobalshortcutsrc --group google-chrome.desktop --key "new-private-window" "none,none,Open new private window"
kwriteconfig5 --file kglobalshortcutsrc --group google-chrome.desktop --key "new-window" "none,none,Open new window"
echo "Google Chrome shortcuts have been configured."

# Configure media control shortcuts
kwriteconfig5 --file kglobalshortcutsrc --group kmix --key "decrease_volume" "Meta+Ctrl+Alt+J,Volume Down,Decrease Volume"
kwriteconfig5 --file kglobalshortcutsrc --group kmix --key "increase_volume" "Meta+Ctrl+Alt+K,Volume Up,Increase Volume"
kwriteconfig5 --file kglobalshortcutsrc --group mediacontrol --key "playpausemedia" "Alt+Space,Media Play,Play/Pause media playback"
echo "Media control shortcuts have been configured."

# Configure kwin shortcuts
kwriteconfig5 --file kglobalshortcutsrc --group plasmashell --key "manage activities" "none,Meta+Q,Show Activity Switcher" # remove Meta+Q default assignment
kwriteconfig5 --file kglobalshortcutsrc --group kwin --key "Window Close" "Meta+Q,Alt+F4,Close Window"
kwriteconfig5 --file kglobalshortcutsrc --group kwin --key "Window Maximize" "Meta+Tab,Meta+PgUp,Maximize Window"
kwriteconfig5 --file kglobalshortcutsrc --group plasmashell --key "activate task manager entry 1" ",Meta+1,Activate Task Manager Entry 1"
kwriteconfig5 --file kglobalshortcutsrc --group plasmashell --key "activate task manager entry 2" ",Meta+2,Activate Task Manager Entry 2"
kwriteconfig5 --file kglobalshortcutsrc --group plasmashell --key "activate task manager entry 3" ",Meta+3,Activate Task Manager Entry 3"
kwriteconfig5 --file kglobalshortcutsrc --group plasmashell --key "activate task manager entry 4" ",Meta+4,Activate Task Manager Entry 4"
kwriteconfig5 --file kglobalshortcutsrc --group plasmashell --key "activate task manager entry 5" ",Meta+5,Activate Task Manager Entry 5"
kwriteconfig5 --file kglobalshortcutsrc --group kwin --key "Switch to Desktop 1" "Meta+1,Ctrl+F1,Switch to Desktop 1"
kwriteconfig5 --file kglobalshortcutsrc --group kwin --key "Switch to Desktop 2" "Meta+2,Ctrl+F2,Switch to Desktop 2"
kwriteconfig5 --file kglobalshortcutsrc --group kwin --key "Switch to Desktop 3" "Meta+3,Ctrl+F3,Switch to Desktop 3"
kwriteconfig5 --file kglobalshortcutsrc --group kwin --key "Switch to Desktop 4" "Meta+4,Ctrl+F4,Switch to Desktop 4"
kwriteconfig5 --file kglobalshortcutsrc --group kwin --key "Switch to Desktop 5" "Meta+5,Ctrl+F5,Switch to Desktop 5"

kwriteconfig5 --file kglobalshortcutsrc --group ksmserver --key "Lock Session" "none,Meta+L Screensaver,Lock Session" # remove Meta+L default assignment
kwriteconfig5 --file kglobalshortcutsrc --group kwin --key "Switch to Next Desktop" "Meta+L,,Switch to Next Desktop"
kwriteconfig5 --file kglobalshortcutsrc --group kwin --key "Switch to Previous Desktop" "Meta+H,,Switch to Next Desktop"
kwriteconfig5 --file kglobalshortcutsrc --group kwin --key "Window One Desktop to the Left" "Meta+Shift+H,Meta+Ctrl+Shift+Left,Window One Desktop to the Left"
kwriteconfig5 --file kglobalshortcutsrc --group kwin --key "Window One Desktop to the Right" "Meta+Shift+L,Meta+Ctrl+Shift+Right,Window One Desktop to the Right"

kwriteconfig5 --file kglobalshortcutsrc --group kwin --key "Window to Desktop 1" "Meta+!,,Window to Desktop 1"
kwriteconfig5 --file kglobalshortcutsrc --group kwin --key "Window to Desktop 2" "Meta+@,,Window to Desktop 2"
kwriteconfig5 --file kglobalshortcutsrc --group kwin --key "Window to Desktop 3" "Meta+#,,Window to Desktop 3"
kwriteconfig5 --file kglobalshortcutsrc --group kwin --key "Window to Desktop 4" "Meta+$,,Window to Desktop 4"
kwriteconfig5 --file kglobalshortcutsrc --group kwin --key "Window to Desktop 5" "Meta+%,,Window to Desktop 5"
echo "KWin shortcuts have been configured."
