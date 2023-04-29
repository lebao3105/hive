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
from .warn_box import *

class FileExplorer(ctk.CTkScrollableFrame):
    def __init__(self, master: ctk.CTk, cwd: str, cwd_var: ctk.StringVar, icon_path: str) -> None:
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

        # current directory setup
        self.cwd = cwd
        os.chdir(self.cwd)

        # start by filling tree
        self.fill_tree(self.cwd, self.sys_files, icon_path) # filling the tree with files and dirs

    def fill_tree(self, cwd: str, sys_files: int, icon_path: str) -> None:
        """
        Fills the file explorer tree with all the files and directories in the current working 
        directory. Is supposed to be called every frame.
        """

        # settin up attributes
        self.sys_files = sys_files
        self.cwd = cwd
        os.chdir(self.cwd)
        entities = os.listdir(self.cwd)

        # sorting our entities to make the file explorer sensible
        entities.sort()

        # grid setup
        self.grid_columnconfigure(0, weight = 0)
        self.grid_columnconfigure(1, weight = 1)
        self.grid_rowconfigure(0, weight = 0)
        for num in range(len(entities)):
            self.grid_rowconfigure(num + 1, weight = 0)

        # clear previous label widgets
        for widget in self.winfo_children():
            widget.destroy()

        # a button to let the user navigate up a directory
        up_label = ctk.CTkLabel(master = self,
                                text = "←"
                                )
        up_label.grid(row = 0,
                      column = 1,
                      padx = PADX,
                      pady = PADY,
                      sticky = "w"
                      )

        up_label.bind("<Double-Button-1>",
                      self.up_one_dir()
                      )

        up_icon = ctk.CTkImage(light_image = Image.open(f"{icon_path}folder.png"))
        up_button = ctk.CTkButton(master = self,
                                  text = "",
                                  image = up_icon,
                                  width = up_icon.cget("size")[0]
                                  )
        up_button.grid(row = 0,
                       column = 0,
                       padx = PADX,
                       pady = PADY,
                       sticky = "w"
                       )

        up_button.bind("<Double-Button-1>",
                    self.up_one_dir()
                    )

        # if we don't want to see system files; 0 = False
        if self.sys_files == 0:
            for entity in entities:
                # create a path to the file/directory
                if self.cwd.endswith("/"):
                    entity_path = f"{self.cwd}{entity}"
                else:
                    entity_path = f"{self.cwd}/{entity}"

                # is the file a hidden system file
                if self.is_hidden(entity, entity_path):
                    pass

                # is the file a normal, user visible file?
                else:
                    label = ctk.CTkLabel(master = self,
                                         text = entity
                                         )
                    label.grid(row = entities.index(entity) + 1,
                               column = 1,
                               padx = PADX,
                               pady = PADY,
                               sticky = "w"
                               )
                    label.bind("<Double-Button-1>",
                               lambda event, text = label.cget("text"):
                               self.open_entity(event, text)
                               )

                    if os.path.isfile(entity_path):
                        if icon_path.endswith("/"):
                            icon = ctk.CTkImage(light_image = Image.open(f"{icon_path}file.png"))
                        else:
                            icon = ctk.CTkImage(light_image = Image.open(f"{icon_path}/file.png"))
                    else:
                        if icon_path.endswith("/"):
                            icon = ctk.CTkImage(light_image = Image.open(f"{icon_path}folder.png"))
                        else:
                            icon = ctk.CTkImage(light_image = Image.open(f"{icon_path}/folder.png"))
                    button = ctk.CTkButton(master = self,
                                           image = icon,
                                           text = "",
                                           width = icon.cget("size")[0]
                                           )
                    button.grid(row = entities.index(entity) + 1,
                                column = 0,
                                padx = PADX,
                                pady = PADY,
                                sticky = "w"
                                )
                    button.bind("<Double-Button-1>",
                                lambda event, text = label.cget("text"):
                                self.open_entity(event, text)
                                )

        # if we want to see system files; 1 = True
        elif self.sys_files == 1:
            for entity in entities:
                if self.cwd.endswith("/"):
                    entity_path = f"{self.cwd}{entity}"
                else:
                    entity_path = f"{self.cwd}/{entity}"

                # for some reason, doesn't work on ".file" - maybe due to permissions
                if entity.startswith(".") or entity_path in self.not_allowed:
                    # magic to move an item to end of list
                    entities.append(entities.pop(entities.index(entity)))

            for entity in entities:
                # create a path to the file/directory
                if self.cwd.endswith("/"):
                    entity_path = f"{self.cwd}{entity}"
                else:
                    entity_path = f"{self.cwd}/{entity}"

                label = ctk.CTkLabel(master = self,
                                     text = entity
                                     )
                label.grid(row = entities.index(entity) + 1,
                           column = 1,
                           padx = PADX,
                           pady = PADY,
                           sticky = "w"
                           )
                label.bind("<Double-Button-1>",
                           lambda event, text = label.cget("text"):
                           self.open_entity(event, text)
                           )

                if os.path.isfile(entity_path):
                    if icon_path.endswith("/"):
                        icon = ctk.CTkImage(light_image = Image.open(f"{icon_path}file.png"))
                    else:
                        icon = ctk.CTkImage(light_image = Image.open(f"{icon_path}/file.png"))
                else:
                    if icon_path.endswith("/"):
                        icon = ctk.CTkImage(light_image = Image.open(f"{icon_path}folder.png"))
                    else:
                        icon = ctk.CTkImage(light_image = Image.open(f"{icon_path}/folder.png"))
                button = ctk.CTkButton(master = self,
                                       image = icon,
                                       text = "",
                                       width = icon.cget("size")[0]
                                       )
                button.grid(row = entities.index(entity) + 1,
                            column = 0,
                            padx = PADX,
                            pady = PADY,
                            sticky = "w"
                            )
                button.bind("<Double-Button-1>",
                            lambda event, text = label.cget("text"):
                            self.open_entity(event, text)
                            )

    def open_entity(self, event, text: str) -> None: # pylint: disable=unused-argument
        """
        An event in the case that the user double clicks a file or directory. Should open the file 
        or directory.
        """

        os.chdir(self.cwd)

        if self.cwd.endswith("/"):
            new_path = f"{self.cwd}{text}"
        else:
            new_path = f"{self.cwd}/{text}"

        if os.path.isfile(new_path) or new_path.endswith(".app"): # a file or application
            run(["open", new_path], check = True)
        else: # a directory
            new_path += "/"
            self.cwd = new_path
            os.chdir(self.cwd)
            self.cwd_var.set(self.cwd)

    def up_one_dir(self) -> None:
        """
        Allow the user to move up one directory. Essential for navigating the file hierarchy.
        """

    def is_hidden(self, entity: str, path: str) -> bool:
        """
        Check if the file/directory at the given path is a hidden system file/directory.
        """

        return (entity.startswith(".")) or (path in self.not_allowed)
