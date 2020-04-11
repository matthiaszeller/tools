# -*- coding: utf-8 -*-

# Applications to launch
# Format: dictionnary, key = workspace, value = list of (app-name, desktop-number, additional)
# desktop-number = -1 means the 2nd monitor
# additional: dic of settings. Example: {'min-sleep':2} for apps taking long time to launch
# Note: must specify in the right order (can't move an app to desktop n°3 if a single desktop is active)
workspaces = {
    'proj':
        [
            ('firefox', -1),
            ('gnome-system-monitor', 0),
            ('gnome-terminal', 1),
            ('pycharm-community', 2)
        ],
    'test':
        [
            ('gnome-system-monitor', 1)
        ]
}


# Name of second screen, get with xrandr
screen_2_name = 'DVI-0'
