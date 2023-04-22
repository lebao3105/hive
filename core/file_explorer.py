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

class FileExplorer(ctk.CTkFrame):
    def __init__(self, master: ctk.CTk):
        """
        The main file explorer widget. This widget displays all the files and directories in the 
        current working directory.
        """

        # widget setup
        super().__init__(master=master,
                         )

        # getting user and path data, filling tree
        self.user = os.environ["USER"]
        self.user_path = f"/Users/{self.user}"
        self.cwd = self.user_path
        self.fill_tree(self.cwd, 0)

    def fill_tree(self, cwd: str, sys_files: int):
        """
        Fills the file explorer tree with all the files and directories in the current working 
        directory. Is supposed to be called every frame.
        """

        # settin up attributes
        self.cwd = cwd
        entities = os.listdir(self.cwd)

        # grid setup
        self.grid_columnconfigure(0, weight = 1)
        for num in range(len(entities)):
            self.grid_rowconfigure(num, weight = 1)

        # adding files and directories to list
        for entity in entities:
            label = ctk.CTkLabel(master = self,
                                 text = entity
                                 )
            label.grid(row = entities.index(entity), column = 0)
