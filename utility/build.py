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

from os import remove
from shutil import rmtree
from subprocess import run
from platform import system
from pathlib import Path
from sys import exit as sys_exit

from PyInstaller.__main__ import run as pkg

# location of the repository
REPO_LOC = Path("./").absolute()

# pip
PIP_CMD = "pip3"

# find where customtkinter is located
output = run([PIP_CMD, "show", "customtkinter"], check = True, capture_output = True).stdout
output = output.split() # split by the newline chars

# convert from bytes to string
for index, item in enumerate(output):
    output[index] = item.decode()

# customtkinter's location
CTK_LOC = Path(output[24])
CTK_LOC /= "customtkinter"

# location of icon file
ICON_LOC = Path(f"{REPO_LOC}/source/icons/dark.png")

# location of other directories that are needed
CORE_LOC = Path(f"{REPO_LOC}/core")
SRC_LOC = Path(f"{REPO_LOC}/source")
CFG_LOC = Path(f"{REPO_LOC}/config")
DIST_LOC = Path(f"{REPO_LOC}/dist")
UTIL_LOC = Path(f"{REPO_LOC}/utility")

# arguments for pyinstaller; these are command line args
ARGS = [f"{REPO_LOC}/hive.py", # file to package
        "-n=hive", # name
        f"-i={ICON_LOC}", # icon
        "--clean", # clear cache
        "--windowed", # no terminal window
        "-y", # no confirmation
        "--onedir", # one directory with all files
        f"--distpath={DIST_LOC}", # location of the build
        f"--specpath={UTIL_LOC}", # location of the .spec file
        "--log-level=ERROR", # verbosity
        f"--add-data={CTK_LOC}:customtkinter", # adds customtkinter module
        f"--add-data={CORE_LOC}:core", # adds core directory
        f"--add-data={SRC_LOC}:source", # adds source directory
        f"--add-data={CFG_LOC}:config" # adds config directory
        ]

if not CFG_LOC.exists():
    ARGS.pop(-1)

# build the application
pkg(ARGS)

# locations of extra files/dirs
extras = [Path(f"{REPO_LOC}/build"),
          Path(f"{REPO_LOC}/dist/hive"),
          Path(f"{REPO_LOC}/utility/hive.spec")
          ]

# remove the extra files and dirs
rmtree(extras[0])
rmtree(extras[1])
remove(extras[2])
