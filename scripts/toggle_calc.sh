#!/bin/bash

# Name of the calculator window (adjust if necessary)
CALC_WINDOW_NAME="Calculator"

# Find the window ID of the calculator
CALC_WINDOW_ID=$(xdotool search --name "$CALC_WINDOW_NAME" | head -1)

# If the calculator window is not visible, bring it to the front
if [ -z "$CALC_WINDOW_ID" ]; then
    kcalc &
else
    # Toggle the visibility of the calculator window
    xdotool windowunmap "$CALC_WINDOW_ID"
fi

