"""
    Plugin for Launching Updates for the RaspberryMC

    FullSystemReset overwrites Kodi and Emulation Station with latest factory default settings.
    MCUpdate updates just kodi with the latest addons, does not overwrite user settings (unless conflicts with update) or favorites.
    MCReset overwrites users addons, settings, favorites to latest factory defaults.
    ESRest resets Emulation Stations to latest factory default settings overwritting users settings, ROMs, and save data
    ESROMUpdates updates just Emulation Stations ROM files (adds new roms to system)
    ESROMReset resets the Emulation Stations ROMs to latest factory defaults overwritting users save data
    Debugging does clear log files

"""

# -*- coding: UTF-8 -*-
# main imports
import sys
import os
import xbmc
import xbmcgui
import xbmcaddon

# plugin constants
__plugin__ = "raspberrymc_updates"
__author__ = "raspberrymc"
__url__ = "http://www.raspberrymc.com"
__credits__ = "RaspberryMC"
__version__ = "0.0.1"
__settings__ = xbmcaddon.Addon(id='plugin.program.raspberrymc_updates')

dialog = xbmcgui.Dialog()

# addon settings values
PREUPDATE = __settings__.getSetting("preUpdate")
MCUPDATE = __settings__.getSetting("mcUpdate")
ESROMUPDATES = __settings__.getSetting("es-rom-updates")
ADULTCONTENT = __settings__.getSetting("adultcontent")
DEBUGGING = __settings__.getSetting("debug")


def clearLog():
    os.popen("/home/osmc/.kodi/addons/plugin.program.raspberrymc_updates/resources/lib/clearlog.sh").read()


def premissionUpdates():
    os.system("sudo chmod 755 /home/osmc/.kodi/addons/plugin.program.raspberrymc_updates/resources/lib/*")


def preupdate():
    xbmc.executebuiltin("ActivateWindow(busydialog)")
    os.popen("/home/osmc/.kodi/addons/plugin.program.raspberrymc_updates/resources/lib/preupdates.sh").read()
    premissionUpdates()
    xbmc.executebuiltin("Dialog.Close(busydialog)")
    dialog.notification("PreUpdate Notification", "Finish running PreUpdate")


def mcupdate():
    xbmc.executebuiltin("ActivateWindow(busydialog)")
    os.popen("/home/osmc/.kodi/addons/plugin.program.raspberrymc_updates/resources/lib/mcupdates.sh").read()
    premissionUpdates()
    xbmc.executebuiltin("Dialog.Close(busydialog)")
    dialog.notification("Update Notification", "Media Center Update Completed", xbmcgui.NOTIFICATION_INFO, 5000)


def esromupdates():
    # TODO: test script, make exclude list for saved game data
    xbmc.executebuiltin("ActivateWindow(busydialog)")
    os.popen("/home/osmc/.kodi/addons/plugin.program.raspberrymc_updates/resources/lib/esromupdates.sh").read()
    dialog.notification("Update Notification", "ES ROM Update Completed", xbmcgui.NOTIFICATION_INFO, 5000)
    xbmc.executebuiltin("Dialog.Close(busydialog)")

def adultcontent():
    # TODO: adultcontent script, exclude from mcupdate
    xbmc.executebuiltin("ActivateWindow(busydialog)")
    #os.popen("/home/osmc/.kodi/addons/plugin.program.raspberrymc_updates/resources/lib/adultcontent.sh").read()
    dialog.notification("Update Notification", "Adult Content Update Completed", xbmcgui.NOTIFICATION_INFO, 5000)
    xbmc.executebuiltin("Dialog.Close(busydialog)")

if DEBUGGING == "false":
    clearLog()

if PREUPDATE == "true":
    dialog.ok("Run PreUpdate", "Check for updates to the RaspberryMC Update Script Files")
    preupdate()
    __settings__.setSetting(id='preUpdate', value='false')


else:
    if dialog.yesno("Update Notification",
                    "It is recommended that you backup your settings before proceeding.  Do you want to continue?"):
        if MCUPDATE == "true":
            dialog.notification('Update Notifications', 'Starting Media Center Updates', xbmcgui.NOTIFICATION_INFO,
                                2500)
            mcupdate()

        if ESROMUPDATES == "true":
            dialog.notification('Update Notification', 'Running ES ROM Updates', xbmcgui.NOTIFICATION_INFO, 2500)
            esromupdates()

        if ADULTCONTENT == "true":
            dialog.notification('Update Notification', 'Starting Updates of Custom User Options', xbmcgui.NOTIFICATION_INFO, 2500)
            adultcontent()

    dialog.ok("Notification", "Update Complete")
