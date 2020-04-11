from setup import *
# import move_win_class
import subprocess
import sys
import time

# Usage: python launch.py <workspace-name>
# workspace-name: as defined in setup.py

# Useful commands of wmctrl:
# -r <window> to select a window
# -t <desktop> to move a window (specified with -r)

run = lambda cmd: subprocess.Popen(cmd)
get = lambda cmd: subprocess.check_output(cmd).decode("utf-8")


def get_class(classname):
    # function to get all windows that belong to a specific window class (application)
    w_list = [l.split()[0] for l in get(["wmctrl", "-l"]).splitlines()]
    return [w for w in w_list if classname in get(["xprop", "-id", w])]


def move(app, desktop):
    app = get_class(app)[0]
    desktop = str(desktop)
    run(['wmctrl', '-ir', app, '-t', desktop])


if __name__ == '__main__':
    workspace_name = sys.argv[1]
    if not workspace_name in workspaces:
        print(workspace_name, 'is not a workspace')
        exit()

    workspace = workspaces[workspace_name]
    sleeping_time = 0.5
    # Run all apps first
    for w in workspace:
        app = w[0]
        run([app])
        # Manage settings
        if len(w) <= 2: continue
        add = w[2]
        if 'min-sleep' in add:
			sleeping_time = max(sleeping_time, add['min-sleep'])

    # Wait a moment (i.e. let the time for the apps to launch)
    time.sleep(sleeping_time)

    # Move to specific desktops
    for w in workspace:
        app = w[0]
        desktop = w[1]
        move(app, desktop)

