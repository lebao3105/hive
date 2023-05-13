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

from .config import *

def is_hidden(entity: str, path: str) -> bool:
    """
    Check if the file/directory at the given path is a hidden system file/directory.
    """

    return (entity.startswith(".")) or (path in SYSTEM_FILES)

def can_rename(path: str) -> bool:
    """
    Checks if it is possible to rename a file or directory based on some conditions.
    """

    if path in NO_RENAME: # if the file is in our list of no-nos
        return False

    if path.startswith("/Library/"): # if the file is in the Library dir
        return False

    if path.startswith("/System/"): # if the file is in the System dir
        return False

    return True
