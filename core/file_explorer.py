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
from subprocess import run

import customtkinter as ctk
from PIL import Image

from .config import *

class FileExplorer(ctk.CTkScrollableFrame):
    def __init__(self, master: ctk.CTk, cwd: str, cwd_var: ctk.StringVar, icon_path: str):
        """
        The main file explorer widget. This widget displays all the files and directories in the 
        current working directory.
        """

        # widget setup
        super().__init__(master = master
                         )
        self.sys_files = 0
        self.cwd_var = cwd_var

        # list of hidden system files
        self.not_allowed = SYSTEM_FILES

        # getting user and path data
        self.user = USER
        self.user_path = USER_PATH
        self.cwd = cwd

        os.chdir(self.cwd) # change to the current dir

        self.fill_tree(self.cwd, self.sys_files, icon_path) # filling the tree with files and dirs

    def fill_tree(self, cwd: str, sys_files: int, icon_path: str):
        """
        Fills the file explorer tree with all the files and directories in the current working 
        directory. Is supposed to be called every frame.
        """

        # settin up attributes
        self.sys_files = sys_files
        self.cwd = cwd
        os.chdir(self.cwd)
        entities = os.listdir(self.cwd)
        entities = sorted(entities)

        # grid setup
        self.grid_columnconfigure(0, weight = 0)
        self.grid_columnconfigure(1, weight = 1)
        for num in range(len(entities)):
            self.grid_rowconfigure(num, weight = 0)

        # clear previous label widgets
        for label in self.winfo_children():
            label.destroy()

        # if we don't want to see system files; 0 = False
        if self.sys_files == 0:
            for entity in entities:
                # create a path to the file/directory
                if self.cwd.endswith("/"):
                    entity_path = f"{self.cwd}{entity}"
                else:
                    entity_path = f"{self.cwd}/{entity}"

                # is the file a hidden system file
                if (entity_path in self.not_allowed) or (self.is_hidden(entity)):
                    pass

                # is the file a normal, user visible file?
                else:
                    label = ctk.CTkLabel(master = self,
                                         text = entity
                                         )
                    label.grid(row = entities.index(entity),
                               column = 1,
                               padx = PADX,
                               pady = PADY,
                               sticky = "w"
                               )
                    label.bind('<Double-Button-1>',
                               lambda event, text = label.cget("text"):
                               self.open_entity(event, text) # pylint: disable=cell-var-from-loop
                               )

                    if os.path.isfile(entity_path):
                        icon = ctk.CTkImage(light_image = Image.open(f"{icon_path}/file.png"))
                    else:
                        icon = ctk.CTkImage(light_image = Image.open(f"{icon_path}/folder.png"))
                    button = ctk.CTkButton(master = self,
                                           image = icon,
                                           text = "",
                                           width = icon.cget("size")[0]
                                           )
                    button.grid(row = entities.index(entity),
                                column = 0,
                                padx = PADX,
                                pady = PADY,
                                sticky = "w"
                                )
                    button.bind('<Double-Button-1>',
                                lambda event, text = label.cget("text"):
                                self.open_entity(event, text) # pylint: disable=cell-var-from-loop
                                )

        # if we want to see system files; 1 = True
        elif self.sys_files == 1:
            for entity in entities:
                # create a path to the file/directory
                if self.cwd.endswith("/"):
                    entity_path = f"{self.cwd}{entity}"
                else:
                    entity_path = f"{self.cwd}/{entity}"

                label = ctk.CTkLabel(master = self,
                                     text = entity
                                     )
                label.grid(row = entities.index(entity),
                           column = 1,
                           padx = PADX,
                           pady = PADY,
                           sticky = "w"
                           )
                label.bind('<Double-Button-1>',
                           lambda event, text = label.cget("text"):
                           self.open_entity(event, text) # pylint: disable=cell-var-from-loop
                           )

                if os.path.isfile(entity_path):
                    icon = ctk.CTkImage(light_image = Image.open(f"{icon_path}/file.png"))
                else:
                    icon = ctk.CTkImage(light_image = Image.open(f"{icon_path}/folder.png"))
                button = ctk.CTkButton(master = self,
                                       image = icon,
                                       text = "",
                                       width = icon.cget("size")[0]
                                       )
                button.grid(row = entities.index(entity),
                            column = 0,
                            padx = PADX,
                            pady = PADY,
                            sticky = "w"
                            )
                button.bind('<Double-Button-1>',
                            lambda event, text = label.cget("text"):
                            self.open_entity(event, text) # pylint: disable=cell-var-from-loop
                            )

    def open_entity(self, event, text: str): # pylint: disable=unused-argument
        """
        An event in the case that the user double clicks a file or directory. Should open the file 
        or directory.
        """

        os.chdir(self.cwd) # change to current directory
        path = os.path.abspath(f"./{text}") # make a path to our entity

        if not os.path.isfile(path) and not path.endswith(".app"): # a directory
            os.chdir(path) # use relative paths to get to the double clicked directory

            if self.cwd.endswith("/"): # if we already have a "/"
                self.cwd = f"{self.cwd}{text}" # change to our new path
            else: # if we don't
                self.cwd = f"{self.cwd}/{text}" # change to our new path
        else: # a file or an app
            run(["open", path], check = True)

        self.cwd_var.set(self.cwd) # set the variable to the new path

    def is_hidden(self, path: str):
        """
        Check if the file/directory at the given path is a hidden system file/directory.
        """

        return path.startswith(".")
