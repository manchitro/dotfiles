#!/usr/bin/env bash

editor=$1
terminal="kitty"
scripts=(/home/s/scripts/*)

choice=$(printf '%s\n' "${scripts[@]}" | sort | rofi -dmenu -p "Edit with $editor" -kb-cancel Alt+F1,Escape)

if [[ "$choice" == "quit" ]]; then
    echo "Program Terminated" && exit 1

elif [ "$choice" ]; then
    cfg=$(echo "$choice" | awk '{print $NF}')
    $terminal -- $editor "$cfg"
    echo "cfg=$cfg"
else
    echo "Program Terminated" && exit 1
fi
