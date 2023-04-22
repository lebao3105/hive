#
#    A whole new file explorer for macOS. Finder, but better.
#    Copyright (C) 2023  Dishant B. (@dishb)
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

import os

import customtkinter as ctk

from .config import *

class FileExplorer(ctk.CTkScrollableFrame):
    def __init__(self, master: ctk.CTk):
        """
        The main file explorer widget. This widget displays all the files and directories in the 
        current working directory.
        """

        # widget setup
        super().__init__(master = master,
                         )
        self.sys_files = 0

        # list of files/dirs that are allowed but start with a "."
        self.files_allowed = [".gitignore",
                              ".github",
                              "pylintrc"
                              ]

        # getting user and path data
        self.user = os.environ["USER"]
        self.user_path = f"/Users/{self.user}"
        self.cwd = self.user_path

        # filling the tree with files and dirs
        self.fill_tree(self.cwd, self.sys_files)

    def fill_tree(self, cwd: str, sys_files: int):
        """
        Fills the file explorer tree with all the files and directories in the current working 
        directory. Is supposed to be called every frame.
        """

        # settin up attributes
        self.sys_files = sys_files
        self.cwd = cwd
        entities = os.listdir(self.cwd)

        # grid setup
        self.grid_columnconfigure(0, weight = 1)
        for num in range(len(entities)):
            self.grid_rowconfigure(num, weight = 0)

        # adding files and directories to list
        for entity in entities:

            # if we don't want to see system files
            if self.sys_files == 0:
                # is the file normal, not starting with a "."?
                if not entity.startswith("."):
                    label = ctk.CTkLabel(master = self,
                                        text = entity
                                        )
                    label.grid(row = entities.index(entity),
                               column = 0,
                               padx = PADX,
                               pady = PADY,
                               sticky = "w"
                               )
                # is the file starting with a ".", but in our exceptions list?
                elif entity.startswith(".") and entity in self.files_allowed:
                    label = ctk.CTkLabel(master = self,
                                        text = entity
                                        )
                    label.grid(row = entities.index(entity), column = 0)
                # is the file starting with a ".", but not in our exceptions list?
                elif entity.startswith(".") and entity not in self.files_allowed:
                    pass

            # if we want to see system files
            elif self.sys_files == 1:
                label = ctk.CTkLabel(master = self,
                                        text = entity
                                        )
                label.grid(row = entities.index(entity),
                           column = 0,
                           padx = PADX,
                           pady = PADY,
                           sticky = "w"
                           )
