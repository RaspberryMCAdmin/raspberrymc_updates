#!/bin/bash

rm -f /home/osmc/.kodi/addons/plugin.program.raspberrymc_updates/resources/logs/update-log.txt
# Copy osmc/kodi from cloud server
rclone copy -v --exclude-from /home/osmc/.kodi/addons/plugin.program.raspberrymc_updates/resources/lib/ignore-list.txt --log-file="/home/osmc/.kodi/addons/plugin.program.raspberrymc_updates/resources/logs/update-log.txt" update_gdrive:AMA_ES/home/osmc/.kodi /home/osmc/.kodi/

# sync Support/tools folder from cloud server
rclone copy -v --log-file="/home/osmc/.kodi/addons/plugin.program.raspberrymc_updates/resources/logs/update-log.txt" update_gdrive:AMA_ES/home/osmc/Support/tools/ /home/osmc/Support/tools/

# update RaspberryMC logo
rclone copy -v --log-file="/home/osmc/.kodi/addons/plugin.program.raspberrymc_updates/resources/logs/update-log.txt" update_gdrive:AMA_ES/home/osmc/Support/tools/images/OSMC.png /usr/share/kodi/addons/skin.osmc/media/OSMC.png

sudo chmod 755 /home/osmc/.kodi/addons/plugin.program.raspberrymc_updates/resources/lib/kodiUpdates.sh
#sudo systemctl restart mediacenter
echo "Update Sync Complete."
exit