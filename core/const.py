#
#    A whole new file explorer for macOS. Finder, but better.
#    Copyright (C) 2023  Dishant B. (@dishb) <code.dishb@gmail.com> and
#    contributors.
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.
#

from os import environ
from os.path import dirname
from sys import platform

# window size
WIDTH = 700
HEIGHT = 600

# design
PADX = 15
PADY = 5

# absolute path to hive.py
SCRIPT_DIR = dirname(__file__).replace("core", "")
if SCRIPT_DIR.endswith("/"):
    SCRIPT_DIR = SCRIPT_DIR.removesuffix("/")

# config file path
CONFIG_PATH = f"{SCRIPT_DIR}/config/settings.cfg"

# path to the theme folder
THEME_PATH = f"{SCRIPT_DIR}/source/themes"

# path to the font folder
FONT_PATH = f"{SCRIPT_DIR}/source/fonts"

# the current user
USER = environ["USER"] if platform != "win32" else environ["USERNAME"]

LIGHT_ICON_PATH = f"{SCRIPT_DIR}/source/icons/light.png"
DARK_ICON_PATH = f"{SCRIPT_DIR}/source/icons/dark.png"

# list of hidden system files/directories
SYSTEM_FILES = ["/bin",
                "/boot",
                "/cores",
                "/private",
                "/etc",
                "/home",
                "/opt",
                "/sbin",
                "/tmp",
                "/usr",
                "/var",
                "/dev",
                "/Volumes",
                "/Users/Shared/adi",
                "/Users/Shared/SC Info",
                f"/Users/{USER}/Library",
                f"/Users/{USER}/Trash",
                "/$Recycle.Bin",
                "/hiberfil.sys",
                "/pagefile.sys",
                "/swapfile.sys",
                "/Windows"
                ]

# list of directories that cannot be renamed
NO_RENAME = ["/Applications",
             "/Library",
             "/System",
             "/Users",
             f"/Users/{USER}",
             "/Users/Shared",
             f"/Users/{USER}/Desktop",
             f"/Users/{USER}/Documents",
             f"/Users/{USER}/Downloads",
             f"/Users/{USER}/Movies",
             f"/Users/{USER}/Music",
             f"/Users/{USER}/Pictures",
             f"/Users/{USER}/Public",
            "/Program Files",
            "/Program Files (x86)"
            ]
NO_RENAME += SYSTEM_FILES