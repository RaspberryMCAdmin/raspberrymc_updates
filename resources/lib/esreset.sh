#!/bin/bash

# Sync RetroPie load screen files from cloud server
rclone sync -v --log-file="/home/osmc/.kodi/addons/plugin.program.raspberrymc_updates/resources/logs/update-log.txt" update_gdrive:AMA_ES/home/RetroPie /home/RetroPie

# Sync RetroPie system and userdata files
rclone sync -v --log-file="/home/osmc/.kodi/addons/plugin.program.raspberrymc_updates/resources/logs/update-log.txt" update_gdrive:AMA_ES/opt/retrosmc /opt/retrosmc

echo "RetroPie Reset Complete."
exit