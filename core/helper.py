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

from os import listdir, mkdir
from os.path import exists

from .config import USER, SYSTEM_FILES, NO_RENAME

def create_dir() -> None:
    """
    Creates a special directory for users to put their custom themes in.
    """

    path = f"/Users/{USER}/.hive/"

    if not exists(path):
        mkdir(path)

def get_all_themes(path: str) -> list:
    """
    Returns a list of all the themes in the given path.
    """

    # local variables
    files = listdir(path)
    files += listdir(f"/Users/{USER}/.hive/")
    themes = []

    # get all the themes (.json files)
    for file in files:

        # call methods on each string to get it ready for user
        file = file.removesuffix(".json")
        file = file.capitalize()

        if "_" in file:
            file = file.replace("_", " ")
            temp = file.split(" ")
            file = ""
            for index, item in enumerate(temp):
                temp[index] = item.capitalize()
                if not index == 0:
                    file += " " + temp[index]
                else:
                    file += temp[index]

        themes.append(file)

    themes.sort()

    # move the default theme to top of list
    old_index = themes.index("Default")
    themes.insert(0, themes.pop(old_index))

    return themes

def is_hidden(entity: str, path: str) -> bool:
    """
    Check if the file/directory at the given path is a hidden system file/directory.
    """

    if entity.startswith("."): # many system files/dirs start with a "."
        return True

    for hidden_path in SYSTEM_FILES:
        if path.startswith(hidden_path): # if the file/dir is a known system file/dir
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
