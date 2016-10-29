#!/usr/bin/env python3
import sys
from gi.repository import Playerctl, GLib
player = Playerctl.Player()

def on_track_change(player, e):
    sys.exit()

player.on('metadata', on_track_change)
GLib.MainLoop().run()
