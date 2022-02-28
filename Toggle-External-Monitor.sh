#!/bin/bash

if xrandr --query | grep 'HDMI-A-0 connected';
then
    xrandr --output HDMI-A-0 --auto --left-of eDP --primary
    ~/.config/polybar/launch.sh
else
    xrandr --output HDMI-A-0 --off
fi
