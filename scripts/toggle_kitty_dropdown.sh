#!/bin/bash

# Check if kitty is installed
if ! command -v kitty &> /dev/null; then
    echo "Kitty terminal is not installed. Please install it."
    exit 1
fi

# Get the current kitty window ID
window_id=$(xdotool search --class kitty | head -1)

# Send the toggle command to kitty
if [ -n "$window_id" ]; then
    xdotool windowfocus $window_id
    xdotool key F12
else
    # If no kitty window found, start a new one
    kitty --single-instance --name=dropdown
fi

