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
    def __init__(self, master: ctk.CTk, cwd: str, cwd_var: ctk.StringVar):
        """
        The main file explorer widget. This widget displays all the files and directories in the 
        current working directory.
        """

        # widget setup
        super().__init__(master = master
                         )
        self.sys_files = 0
        self.cwd_var = cwd_var

        # list of files/dirs that are allowed but start with a "."
        self.allowed = [".gitignore",
                        ".github",
                        ".pylintrc"
                        ]

        # list of files/dirs that aren't allowed and don't start with a "."
        self.not_allowed = ["usr",
                            "home",
                            "bin",
                            "sbin",
                            "var",
                            "private",
                            "opt",
                            "dev",
                            "cores",
                            "tmp",
                            "etc",
                            "Volumes"
                            ]

        # getting user and path data
        self.user = os.environ["USER"]
        self.user_path = f"/Users/{self.user}/"
        self.cwd = cwd

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
        os.chdir(self.cwd)
        entities = os.listdir(self.cwd)

        # grid setup
        self.grid_columnconfigure(0, weight = 1)
        for num in range(len(entities)):
            self.grid_rowconfigure(num, weight = 0)

        # clear previous label widgets
        for label in self.winfo_children():
            label.destroy()

        # if we don't want to see system files; 0 = False
        if self.sys_files == 0:
            for entity in entities:
                # is the file not starting with a "." and in our not allowed list?
                if entity in self.not_allowed:
                    pass

                # is the file a normal, user visible file?
                elif not entity.startswith("."):
                    label = ctk.CTkLabel(master = self,
                                         text = entity
                                         )
                    label.grid(row = entities.index(entity),
                               column = 0,
                               padx = PADX,
                               pady = PADY,
                               sticky = "w"
                               )
                    label.bind('<Double-Button-1>',
                               lambda event: self.open_entity(event, label.cget("text")) # pylint: disable=cell-var-from-loop
                               )

                # is the file starting with a ".", but in our exceptions list?
                elif entity.startswith(".") and entity in self.allowed:
                    label = ctk.CTkLabel(master = self,
                                         text = entity
                                         )
                    label.grid(row = entities.index(entity),
                               column = 0,
                               padx = PADX,
                               pady = PADY,
                               sticky = "w"
                               )
                    label.bind('<Double-Button-1>',
                               lambda event: self.open_entity(event, label.cget("text")) # pylint: disable=cell-var-from-loop
                               )

                # is the file starting with a ".", but not in our exceptions list?
                elif entity.startswith(".") and entity not in self.allowed:
                    pass

        # if we want to see system files; 1 = True
        elif self.sys_files == 1:
            for entity in entities:
                label = ctk.CTkLabel(master = self,
                                     text = entity
                                     )
                label.grid(row = entities.index(entity),
                           column = 0,
                           padx = PADX,
                           pady = PADY,
                           sticky = "w"
                           )
                label.bind('<Double-Button-1>',
                           lambda event: self.open_entity(event, label.cget("text")) # pylint: disable=cell-var-from-loop
                           )

    def open_entity(self, event, text: str): # pylint: disable=unused-argument
        """
        An event in the case that the user double clicks a file or directory. Should open the file 
        or directory.
        """

        os.chdir(self.cwd) # change to current directory
        os.chdir(f"./{text}") # use relative paths to get to the double clicked directory
        self.cwd = f"{self.cwd}{text}" # change to our new path
        self.cwd_var.set(self.cwd) # set the variable to the new path
