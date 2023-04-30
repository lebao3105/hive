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

# window size
WIDTH = 700
HEIGHT = 600

# design
PADX = 15
PADY = 5

# paths to files and directories
SCRIPT_DIR = dirname(__file__).replace("core", "")
if SCRIPT_DIR.endswith("/"):
    SCRIPT_DIR = SCRIPT_DIR.removesuffix("/")
THEME_PATH = f"{SCRIPT_DIR}/src/themes/hive_theme.json"
USER = environ["USER"]

LIGHT_ICON_PATH = f"{SCRIPT_DIR}/src/icons/light.png"
DARK_ICON_PATH = f"{SCRIPT_DIR}/src/icons/dark.png"

# list of hidden system files/directories
SYSTEM_FILES = ["/bin",
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
                f"/Users/{USER}/Trash"
                ]
