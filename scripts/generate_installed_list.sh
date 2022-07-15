#!/bin/sh

pacman -Qe > /home/s/.installed-packages-pac
pacman -Qm > /home/s/.installed-packages-aur
