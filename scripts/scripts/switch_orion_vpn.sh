#!/usr/bin/env bash

if nmcli con show --active | grep -q 'Orion'; then
        nmcli con down id Orion;
        if nmcli con show --active | grep -q 'F3'; then
                nmcli con down id Tether;
        fi
nmcli con up id Future;
else
        if nmcli con show --active | grep -q 'Future'; then
                nmcli con down id Future;
        fi
        if nmcli con show --active | grep -q 'F3'; then
                nmcli con up id Orion;
        else
                nmcli con up id Tether;
                nmcli con up id Orion;
        fi
fi

exit 1;
