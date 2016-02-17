#!/bin/bash

# Sync RetroPie ROM files from cloud server
rclone sync -v --log-file="/home/osmc/.kodi/addons/plugin.program.raspberrymc_updates/resources/logs/update-log.txt" update_gdrive:AMA_ES/opt/retrosmc/home/pi/RetroPie/roms /opt/retrosmc/home/pi/RetroPie/roms

echo "RetroPie Update Complete."
exit