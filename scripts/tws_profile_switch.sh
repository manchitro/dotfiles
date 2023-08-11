#!/usr/bin/env bash

if pacmd list-cards | grep -q -e "active profile: <a2dp_sink>"; then
    pacmd set-card-profile bluez_card.FC_E8_06_16_0C_AA handsfree_head_unit;
elif pacmd list-cards | grep -q -e "active profile: <handsfree_head_unit>"; then
    pacmd set-card-profile bluez_card.FC_E8_06_16_0C_AA a2dp_sink;
fi

exit 1;
