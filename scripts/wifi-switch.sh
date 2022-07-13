#!/usr/bin/env bash

if nmcli con show --active | grep -q 'Future'; then
	echo 'Future->Phone'
elif nmcli con show --active | grep -q 'Phone'; then
	echo 'Phone->Future'
fi

exit 1;
