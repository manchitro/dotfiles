#!/usr/bin/env bash

editor=$1
terminal="kitty"

declare -a options=(
"hosts - /etc/hosts"
"fish user key bindings - .config/fish/functions/fish_user_key_bindings.fish"
".config launcher settings - scripts/confedit.sh"
"Scripts Editor - scripts/scriptedit.sh"
"qtile config - .config/qtile/config.py"
"picom config - .config/picom/picom.conf"
"qtile autostart - .config/qtile/autostart.sh"
"kitty config - .config/kitty/kitty.conf"
"kitty grab config - .config/kitty/grab.conf"
"awesome config - .config/awesome/rc.lua"
"bashrc - .bashrc"
"vimrc - .vimrc"
"greenclip clipboard manager - .config/greenclip.toml"
"fish greeting - .config/fish/functions/fish_greeting.fish"
"rifle config - .config/ranger/rifle.conf"
"fish prompt - .config/fish/functions/fish_prompt.fish"
"fish config - .config/fish/config.fish"
"fish variables - .config/fish/fish_variables"
"neofetch config - .config/neofetch/config.conf"
"ideavimrc - .ideavimrc"
"rofi config - .config/rofi/config.rasi"
"rofi wifi menu - scripts/rofi-wifi-menu.sh"
"xinitrc - .xinitrc"
"powerline-shell - .config/powerline-shell/config.json"
"betterlockscreen - .config/betterlockscreenrc"
"deadd config - .config/deadd/deadd.yml"
"deadd css - .config/deadd/deadd.css"
"ranger config - .config/ranger/rc.conf"
"ranger scope config - .config/ranger/scope.sh"
"pac installed - .installed-packages-pac"
"aur installed - .installed-packages-aur"
"libinput gestures - .config/libinput-gestures.conf"
"dunst config - .config/dunst/dunstrc"
"conky config - .config/conky/conky.conf"
"eww config - .config/eww/"
"keynav config - .keynavrc"
"pacman config - /etc/pacman.conf"
"gtk3 config - .config/gtk-3.0/settings.ini"
"neovim config - .config/nvim/init.lua"
"mpv config - .config/mpv/mpv.conf"
"autostart - autostart.sh"
"tmux - .config/tmux/tmux.conf"
"quit"
)

choice=$(printf '%s\n' "${options[@]}" | sort | rofi -dmenu -i -p "Edit with $editor" -kb-cancel Alt+F1,Escape)
#choice=$(printf '%s\n' "${options[@]}" | sort | dmenu -i -l 20 -p 'Edit Config:')

if [[ "$choice" == "quit" ]]; then
    echo "Program Terminated" && exit 1

elif [ "$choice" ]; then
    cfg=$(echo "$choice" | awk '{print $NF}')
    if command -v tmux &>/dev/null; then
        tmux split-window -h "$editor $cfg"
    else 
        $terminal -- $editor "$cfg"
    fi
    echo "cfg=$cfg"
else
    echo "Program Terminated" && exit 1
fi
