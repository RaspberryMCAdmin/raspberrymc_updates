#!/bin/bash

# Copy osmc/kodi from cloud server
rclone sync -v --log-file="/home/osmc/.kodi/addons/plugin.program.raspberrymc_updates/resources/logs/update-log.txt" update_gdrive:AMA_ES/home/osmc/.kodi/addons/plugin.program.raspberrymc_updates/ /home/osmc/.kodi/addons/plugin.program.raspberrymc_updates/

./home/osmc/Support/tools/

exit