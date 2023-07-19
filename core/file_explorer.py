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

import os
from subprocess import run
from sys import platform

import customtkinter as ctk
from PIL import Image

from .const import PADX, PADY, SCRIPT_DIR
from .helper import can_rename, is_hidden
from .popup import ErrorBox, WarnBox
from .rename import RenamePopup
from .extensions import CTkXYFrame

class FileExplorer(CTkXYFrame):
    def __init__(self,
                 master: ctk.CTk,
                 cwd: str,
                 cwd_var: ctk.StringVar,
                 icon_path: str,
                 font: tuple
                 ) -> None:
        """
        The main file explorer widget. This widget displays all the files and directories in the 
        current working directory.
        """

        # widget setup
        super().__init__(master = master
                         )
        self.sys_files = 0
        self.cwd_var = cwd_var

        # create an empty variable for later use
        self.rename_popup = None

        # font setup
        self.font = font

        # current directory setup
        self.cwd = cwd
        os.chdir(self.cwd)

        # start by filling tree
        self.icon_path = icon_path
        self.fill_tree(self.cwd, self.sys_files) # filling the tree with files and dirs

    def fill_tree(self, cwd: str, sys_files: int) -> None:
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

        if not self.cwd in ["/", os.getenv("SYSTEMDRIVE")]:
            # a button to let the user navigate up a directory
            up_label = ctk.CTkLabel(master = self,
                                    text = "←",
                                    font = self.font
                                    )
            up_label.grid(row = 0,
                        column = 1,
                        padx = PADX,
                        pady = PADY,
                        sticky = "w"
                        )

            up_label.bind("<Double-Button-1>",
                        self.up_one_dir
                        )

            up_icon = ctk.CTkImage(light_image = Image.open(f"{self.icon_path}folder.png"))
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
                        lambda event: # pylint: disable=unnecessary-lambda
                            self.up_one_dir(event)
                        )

        for entity in entities:
            # create a path to the file/directory
            if self.cwd.endswith("/"):
                entity_path = f"{self.cwd}{entity}"
            else:
                entity_path = f"{self.cwd}/{entity}"

            # is the file a hidden system file
            if is_hidden(entity, entity_path) and self.sys_files == 0:
                pass

            # is the file a normal, user visible file?
            else:
                label = ctk.CTkLabel(master = self,
                                        text = entity,
                                        font = self.font
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
                label.bind("<Button-2>",
                            lambda event, text = label.cget("text"):
                                self.rename_entity(event, text)
                            )

                if os.path.isfile(entity_path):
                    if self.icon_path.endswith("/"):
                        icon = ctk.CTkImage(light_image =
                                            Image.open(f"{self.icon_path}file.png")
                                            )
                    else:
                        icon = ctk.CTkImage(light_image =
                                            Image.open(f"{self.icon_path}/file.png")
                                            )
                else:
                    if self.icon_path.endswith("/"):
                        icon = ctk.CTkImage(light_image =
                                            Image.open(f"{self.icon_path}folder.png")
                                            )
                    else:
                        icon = ctk.CTkImage(light_image =
                                            Image.open(f"{self.icon_path}/folder.png")
                                            )
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
                button.bind("<Button-2>",
                            lambda event, text = label.cget("text"):
                                self.rename_entity(event, text)
                            )

    def open_entity(self, event, text: str) -> None: # pylint: disable=unused-argument
        """
        An event in the case that the user double clicks a file or directory.
        Should open the file or directory.
        """

        os.chdir(self.cwd)

        try:
            if self.cwd.endswith("/"):
                new_path = f"{self.cwd}{text}"
            else:
                new_path = f"{self.cwd}/{text}"

            if os.path.isfile(new_path): # is a file

                if platform == "darwin":
                    run(["open", new_path], check = True)
                elif platform == "win32":
                    run(["cmd", new_path], check = True)
                else: # Not a good way.
                    run(new_path, check = True)

            else: # a directory

                new_path += "/"
                self.cwd = new_path
                os.chdir(self.cwd)
                self.cwd_var.set(self.cwd)

        except PermissionError:

            WarnBox(f"{SCRIPT_DIR}/source/misc/warning.png",
                    "Error: This is a system\nfile or directory and should\nnot be modified.",
                    self.font
                    )

    def rename_entity(self, event, text: str) -> None: # pylint: disable=unused-argument
        """
        Allows the use to rename a file or directory,
        """

        os.chdir(self.cwd)

        if self.cwd.endswith("/"):
            path = f"{self.cwd}{text}"
        else:
            path = f"{self.cwd}/{text}"

        # stop the user from renaming
        if not can_rename(text, path):
            ErrorBox(f"Permission denied: {path}")
            raise PermissionError(f"Unable to rename {path} yet. Are you have premission to this path?")
        
        try:
            self.rename_popup = RenamePopup(self.font)
            new_name = self.rename_popup.get_input()

            self.cwd += "/" if not self.cwd.endswith("/") else ""
            new_path = f"{self.cwd}{new_name}"

            # only rename if valid name was entered
            if new_name is not None and new_name != "":
                os.rename(path, new_path)
                self.fill_tree(self.cwd, self.sys_files)

        except Exception as e:
            ErrorBox(f"An error occured when renaming {path}: {e}")

    def up_one_dir(self, event) -> None: # pylint: disable=unused-argument
        """
        Allow the user to move up one directory. Essential for navigating the file hierarchy.
        """

        os.chdir(self.cwd)

        # use relative paths and os module to move to parent dir
        new_path = os.path.abspath("..")
        self.cwd = new_path
        os.chdir(self.cwd)
        self.cwd_var.set(self.cwd)
