#!/usr/bin/env bash

editor=$1
terminal="kitty"

declare -a options=(
"fish user key bindings - .config/fish/functions/fish_user_key_bindings.fish"
"Conf Editor - scripts/confedit.sh"
"Scripts Editor - scripts/scriptedit.sh"
"qtile config - .config/qtile/config.py"
"picom config - .config/picom/picom.conf"
"qtile autostart - .config/qtile/autostart.sh"
"kitty config - .config/kitty/kitty.conf"
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
"dunst config - .config/dunst/dunstrc"
"quit"
)

choice=$(printf '%s\n' "${options[@]}" | sort | rofi -dmenu -p "Edit with $editor" -kb-cancel Alt+F1,Escape)
#choice=$(printf '%s\n' "${options[@]}" | sort | dmenu -i -l 20 -p 'Edit Config:')

if [[ "$choice" == "quit" ]]; then
    echo "Program Terminated" && exit 1

elif [ "$choice" ]; then
    cfg=$(echo "$choice" | awk '{print $NF}')
    $terminal -- $editor "$cfg"
    echo "cfg=$cfg"
else
    echo "Program Terminated" && exit 1
fi
