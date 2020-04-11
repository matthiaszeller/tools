# Tools

Toolbox for linux. The repository is typically located in home folder for easy acces
on startup. 

## Workspace management [prototype]

#### Aim

Run [launch.py](workspace/launch.py) to automatically run applications and move them to specific desktop / screen. 
Setup the environments (e.g. `projectA`) in [setup.py](workspace/setup.py).

#### Example

If the dictionnary `workspace` in [setup.py](workspace/setup.py) contains:

    'proj':
    [
        ('firefox', -1),
        ('gnome-system-monitor', 0),
        ('gnome-terminal', 1),
        ('pycharm-community', 2, {'min-sleep':3})
    ]

Then [launch.py](workspace/launch.py) will:

* run firefox on the second screen *(not functional yet)*
* run `gnome-system-monitor` and move on desktop 0
* run `genome-terminal` and move on desktop 1
* run `pycharm-community`, sleep 3 seconds and move on desktop 2

#### TODO

* Move an app to another screen and maximize it
* Add a setting `command` to be able to run commands if the application is the terminal





