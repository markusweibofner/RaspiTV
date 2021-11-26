#!/bin/bash
var=$(python3 cnbclink.py)
export DISPLAY=:0
vlc -f $var
