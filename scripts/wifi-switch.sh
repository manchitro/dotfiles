#!/usr/bin/env bash

if nmcli con show --active | grep -q 'Future'; then
    nmcli con up "Sazid's Phone"
	echo 'Future->Phone'
elif nmcli con show --active | grep -q 'Phone'; then
    nmcli con up "Future"
	echo 'Phone->Future'
else
    nmcli con up "Future"
	echo 'Future'
fi

exit 1;
