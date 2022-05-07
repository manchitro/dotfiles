#!/usr/bin/env bash

if protonvpn-cli status | grep -q 'Country'; then
	protonvpn-cli d
else
	gnome-terminal -- protonvpn-cli c
fi

exit 1;
