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

from os.path import dirname
from os import remove
from shutil import rmtree
from subprocess import run
from platform import system
from sys import exit as sys_exit

from PyInstaller.__main__ import run as pkg

if system().lower() != "darwin":
    print("You are on an incompatible operating system. hive was designed for and tested on macOS.")
    sys_exit(1)

# location of the repository
REPO_LOC = dirname(__file__).replace("utility", "")
if REPO_LOC.endswith("/"):
    REPO_LOC = REPO_LOC.removesuffix("/")

# find where customtkinter is located
output = run(["pip3", "show", "customtkinter"], check = True, capture_output = True).stdout
output = output.split() # split by the newline chars

# convert from bytes to string
for index, item in enumerate(output):
    output[index] = item.decode()

# customtkinter's location
CTK_LOC = output[24]

# arguments for pyinstaller; these are command line args
ARGS = [f"{REPO_LOC}/hive.py", # file to package
        "-n=hive", # name
        f"-i={REPO_LOC}/source/icons/dark.png", # icon
        "--clean", # clear cache
        "--windowed", # no terminal window
        "-y", # no confirmation
        "--onedir", # one directory with all files
        f"--distpath={REPO_LOC}/dist/", # location of the build
        f"--specpath={REPO_LOC}/utility/", # location of the .spec file
        "--log-level=ERROR", # verbosity
        f"--add-data={CTK_LOC}/customtkinter:customtkinter", # adds customtkinter module
        f"--add-data={REPO_LOC}/core:core", # adds core directory
        f"--add-data={REPO_LOC}/source:source", # adds source directory
        f"--add-data={REPO_LOC}/config:config" # adds config directory
        ]

# build the application
pkg(ARGS)

# remove the extra files and dirs
rmtree(f"{REPO_LOC}/build/")
rmtree(f"{REPO_LOC}/dist/hive/")
remove(f"{REPO_LOC}/utility/hive.spec")
