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
from sys import executable, platform
from shutil import rmtree
from subprocess import run
from pathlib import Path
from argparse import ArgumentParser

from customtkinter import __file__ as ctkpath
from PyInstaller.__main__ import run as pkg

# location of the repository
REPO_LOC = Path("./").absolute()

# pip
PIP_CMD = executable + " -m pip"

# find where customtkinter is located
CTK_LOC = Path(ctkpath).parent.absolute().__str__()

# Path separator
# Use for Pyinstaller's --add-data flag: https://pyinstaller.org/en/stable/usage.html#cmdoption-add-data
# On Windows, it's ";", else it will be ":"
# Don't use os.pathsep yet because it may point to pathsep on posixpath, which is not for Windows.
PATHSEP = ";" if platform == "win32" else ":"

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
        "-n=hive", # name,
        f"-i={ICON_LOC}", # icon
        "--clean", # clear cache
        "--windowed", # no terminal window
        "-y", # no confirmation
        "--onedir", # one directory with all files
        f"--distpath={DIST_LOC}", # location of the build
        f"--specpath={UTIL_LOC}", # location of the .spec file
        "--log-level=ERROR", # verbosity
        f"--add-data={CTK_LOC}{PATHSEP}customtkinter", # adds customtkinter module
        f"--add-data={CORE_LOC}{PATHSEP}core", # adds core directory
        f"--add-data={SRC_LOC}{PATHSEP}source", # adds source directory
        f"--add-data={CFG_LOC}{PATHSEP}config" # adds config directory
        ]

if not CFG_LOC.exists():
    ARGS.pop(-1)

# build the application
# pkg(ARGS)

# locations of extra files/dirs
extras = [Path(f"{REPO_LOC}/build"),
          Path(f"{REPO_LOC}/dist/hive"),
          Path(f"{REPO_LOC}/utility/hive.spec")
          ]

# arguments.
argparser = ArgumentParser(description="Build script for Hive project.")
argparser.add_argument(
    "--build",
    "-b",
    action="store_true",
    help="Build the project (using pyinstaller)"
)
argparser.add_argument(
    "--clean",
    "-c",
    action="store_true",
    help="Remove all built outputs"
)

if __name__ == "__main__":
    args = argparser.parse_args()

    if args.build:
        pkg(ARGS)
    
    if args.clean:
        # not really a good idea(?), but this time we only have these 3 things to remove
        # the pyinstaller build outputs.
        rmtree(extras[0])
        rmtree(extras[1])
        remove(extras[2])