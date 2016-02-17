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
FULLSYSTEMRESET = __settings__.getSetting("full-system-reset")
MCUPDATE = __settings__.getSetting("mcUpdate")
PREUPDATE = __settings__.getSetting("preUpdate")
MCRESET = __settings__.getSetting("mc-reset")
ESROMUPDATES = __settings__.getSetting("es-rom-updates")
ESROMRESET = __settings__.getSetting("es-rom-reset")
ESRESET = __settings__.getSetting("es-reset")
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

def mcreset():
    # TODO: test script
    xbmc.executebuiltin("ActivateWindow(busydialog)")
    os.popen("/home/osmc/.kodi/addons/plugin.program.raspberrymc_updates/resources/lib/mcreset.sh").read()
    premissionUpdates()
    dialog.notification("Reset Notification", "Media Center Reset Completed", xbmcgui.NOTIFICATION_INFO, 5000)
    xbmc.executebuiltin("Dialog.Close(busydialog)")

def esromupdates():
    # TODO: test script, make exclude list for saved game data
    xbmc.executebuiltin("ActivateWindow(busydialog)")
    os.popen("/home/osmc/.kodi/addons/plugin.program.raspberrymc_updates/resources/lib/esromupdates.sh").read()
    dialog.notification("Update Notification", "ES ROM Update Completed", xbmcgui.NOTIFICATION_INFO, 5000)
    xbmc.executebuiltin("Dialog.Close(busydialog)")

def esromreset():
    # TODO: test script
    xbmc.executebuiltin("ActivateWindow(busydialog)")
    os.popen("/home/osmc/.kodi/addons/plugin.program.raspberrymc_updates/resources/lib/esromreset.sh").read()
    dialog.notification("Reset Notification", "ES ROM Reset Completed", xbmcgui.NOTIFICATION_INFO, 5000)
    xbmc.executebuiltin("Dialog.Close(busydialog)")

def esreset():
    # TODO: test script
    xbmc.executebuiltin("ActivateWindow(busydialog)")
    os.popen("/home/osmc/.kodi/addons/plugin.program.raspberrymc_updates/resources/lib/esreset.sh").read()
    dialog.notification("Reset Notification", "ES Reset Completed", xbmcgui.NOTIFICATION_INFO, 5000)
    xbmc.executebuiltin("Dialog.Close(busydialog)")



if DEBUGGING == "false":
    clearLog()

if PREUPDATE == "true":
    dialog.ok("Run PreUpdate", "Check for updates to the", "RaspberryMC Update Script Files")
    preupdate()
    __settings__.setSetting(id='preUpdate', value='false')

elif FULLSYSTEMRESET == "true":
    if dialog.yesno("System Reset Notification", "Running a system reset will overwrite all user data back to the latest factory default settings.  Do you want to continue?"):
        # TODO: create the Full System Reset script
        __settings__.setSetting(id='full-system-reset', value='false')
        dialog.ok("Running Full System Reset", "Test successful", "Function still needs work!")

elif MCRESET == "true":
        if dialog.yesno("MC Reset Notification", "Running a mediacenter reset will overwrite all user data back to the latest factory default settings.  Do you want to continue?"):
            dialog.notification('Reset Notifications', 'Resetting Add-ons back to latest factory default settings.', xbmcgui.NOTIFICATION_INFO, 5000)
            mcreset()
            __settings__.setSetting(id='mc-reset', value='false')
            if dialog.yesno("Reset Notification", "Media Center Reset Complete", "Restart System Now"):
                xbmc.executebuiltin("Reboot")
        else:
            __settings__.setSetting(id='mc-reset', value='false')

elif ESRESET == "true":
    if dialog.yesno("ES Reset Notification", "Running a system restore will overwrite all user data back to the latest factory default settings.  Do you want to continue?"):
        esreset()
        dialog.ok('Reset Notifications', 'Emaulation Station Reset Complete')
    __settings__.setSetting(id='es-reset', value='false')

elif ESROMRESET == "true":
    if dialog.yesno("ES Reset Notification", "Running a system restore will overwrite all user data back to the latest factory default settings.  Do you want to continue?"):
        esromreset()
        dialog.ok('Reset Notifications', 'ES ROM Reset completed')
    __settings__.setSetting(id='es-rom-reset', value='false')

else:
    if dialog.yesno("Update Notification", "It is recommended to backup your settings before proceeding.  Do you want to continue?"):
        if MCUPDATE == "true":
            dialog.notification('Update Notifications', 'Starting Media Center Updates', xbmcgui.NOTIFICATION_INFO, 5000)
            mcupdate()

        if ESROMUPDATES == "true":
            dialog.notification('Reset Notifications', 'Running ES ROM Updates', xbmcgui.NOTIFICATION_INFO, 5000)
            esromupdates()

    dialog.ok("Notification", "Update Complete")