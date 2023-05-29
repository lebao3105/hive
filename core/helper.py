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

from webbrowser import open as open_link

from .config import *

def is_hidden(entity: str, path: str) -> bool:
    """
    Check if the file/directory at the given path is a hidden system file/directory.
    """

    if entity.startswith("."): # many system files/dirs start with a "."
        return True

    if path in SYSTEM_FILES: # if the file/dir is a known system file/dir
        return True

    return False
def can_rename(entity: str, path: str) -> bool:
    """
    Checks if it is possible to rename a file or directory based on some conditions.
    """

    if path in NO_RENAME: # if the file/dir is in our list of no-nos
        return False

    if path.startswith("/Library/"): # if the file/dir is in the Library dir
        return False

    if path.startswith("/System/"): # if the file/dir is in the System dir
        return False

    if is_hidden(entity, path): # if the file/dir is a system file/dir
        return False

    return True

def open_contribute() -> None:
    """
    Opens a link to the official Github repository.
    """

    open_link("https://github.com/dishb/hive")

def open_creator() -> None:
    """
    Opens a link to @dishb on Github.
    """

    open_link("https://github.com/dishb")
