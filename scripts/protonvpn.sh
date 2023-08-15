#!/usr/bin/env bash

if protonvpn-cli status | grep -q 'Country'; then
	protonvpn-cli d
else
	protonvpn-cli r
fi

exit 1;
