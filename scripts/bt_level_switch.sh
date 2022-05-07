#!/usr/bin/env bash

if gnome-extensions info bluetooth-battery@manchitro | grep -q 'DISABLED'; then
	result=$(gnome-extensions info bluetooth-battery@manchitro | grep -e 'Status')
	echo $result
	gnome-extensions enable bluetooth-battery@manchitro
else
	result=$(gnome-extensions info bluetooth-battery@manchitro | grep -e 'Status')
	echo $result
	gnome-extensions disable bluetooth-battery@manchitro
fi

exit 1;
