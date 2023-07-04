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

from json import dump, load
from sys import exit as sys_exit
from os import mkdir
from os.path import exists, isfile, expanduser

import customtkinter as ctk
from PIL import ImageTk, Image

from core import *

class HiveApp(ctk.CTk):
    def __init__(self) -> None:
        """
        Main app class that contains all the widgets and logic. To run, simply create an instance of
        the class and call the ".mainloop()" method on the instance.
        """

        # window setup
        super().__init__()
        self.title("hive")
        self.geometry(f"{WIDTH}x{HEIGHT}")
        self.resizable(True, True)
        self.minsize(200, 200)

        # font setup
        ctk.FontManager.load_font(f"{FONT_PATH}DM Mono.ttf")
        self.font = ("DM Mono", 13)

        # empty widgets for later use
        self.goto_popup = None

        # create a special dir for user-made themes
        create_dir()

        # rows (layout)
        self.grid_rowconfigure(0, weight = 0)
        self.grid_rowconfigure(1, weight = 0)
        self.grid_rowconfigure(2, weight = 0)
        self.grid_rowconfigure(3, weight = 0)
        self.grid_rowconfigure(4, weight = 0)
        self.grid_rowconfigure(5, weight = 0)
        self.grid_rowconfigure(6, weight = 0)
        self.grid_rowconfigure(7, weight = 0)
        self.grid_rowconfigure(8, weight = 0)
        self.grid_rowconfigure(9, weight = 0)
        self.grid_rowconfigure(10, weight = 1)
        self.grid_rowconfigure(11, weight = 0)

        # columns (layout)
        self.grid_columnconfigure(0, weight = 0)
        self.grid_columnconfigure(1, weight = 1)

        # data
        self.cwd_var = ctk.StringVar(master = self,
                                     value = "/"
                                     )
        self.sys_files_var = ctk.IntVar(master = self,
                                        value = 0
                                        )

        # tries to load recent config
        self.open_recent()

        # appearance widgets
        self.appearance_label = AppearanceLabel(self, self.font)
        self.appearance_label.grid(row = 0,
                                   column = 0,
                                   padx = PADX,
                                   pady = PADY,
                                   sticky = "w"
                                   )

        self.appearance_menu = AppearanceMenu(self, self.font)
        self.appearance_menu.grid(row = 1,
                                  column = 0,
                                  padx = PADX,
                                  pady = PADY,
                                  sticky = "w"
                                  )

        # theme widgets
        self.theme_label = ThemeLabel(self, self.font)
        self.theme_label.grid(row = 2,
                              column = 0,
                              padx = PADX,
                              pady = PADY,
                              sticky = "w"
                              )

        # theme widgets
        self.theme_menu = ThemeMenu(self, self.font)
        self.theme_menu.grid(row = 3,
                             column = 0,
                             padx = PADX,
                             pady = PADY,
                             sticky = "w"
                             )
        self.theme_menu.set(self.theme_name)

        # sys files widgets
        self.sys_files_label = SysFilesLabel(self, self.font)
        self.sys_files_label.grid(row = 4,
                                  column = 0,
                                  padx = PADX,
                                  pady = PADY,
                                  sticky = "w"
                                  )

        self.sys_files_switch = SysFilesSwitch(self, self.sys_files_var)
        self.sys_files_switch.grid(row = 5,
                                   column = 0,
                                   padx = PADX,
                                   pady = PADY,
                                   sticky = "w"
                                   )

        # UI scale widgets
        self.scale_label = ScaleLabel(self, self.font)
        self.scale_label.grid(row = 6,
                              column = 0,
                              padx = PADX,
                              pady = PADY,
                              sticky = "w"
                              )

        self.scale_menu = ScaleMenu(self, self.font)
        self.scale_menu.grid(row = 7,
                             column = 0,
                             padx = PADX,
                             pady = PADY,
                             sticky = "w"
                             )
        self.scale_menu.set(self.scale_percent)

        # font widgets
        self.font_label = FontLabel(self, self.font)
        self.font_label.grid(row = 8,
                             column = 0,
                             padx = PADX,
                             pady = PADY,
                             sticky = "w"
                             )

        self.font_menu = FontMenu(self, self.font)
        self.font_menu.grid(row = 9,
                            column = 0,
                            padx = PADX,
                            pady = PADY,
                            sticky = "w"
                            )
        self.font_menu.set(self.font_name)

        # path text (breadcrumbs) widgets
        self.path_text = PathLabel(self,
                                   self.cwd_var.get(),
                                   self.font
                                   )

        self.path_text.grid(row = 11,
                            column = 1,
                            padx = PADX,
                            pady = PADY,
                            sticky = "sw"
                            )

        # attribute setup
        self.file_icon_path = f"{SCRIPT_DIR}/source/file_icons/"

        # file explorer widgets
        self.file_explorer = FileExplorer(self,
                                          self.cwd_var.get(),
                                          self.cwd_var,
                                          self.file_icon_path,
                                          self.font
                                          )
        self.file_explorer.grid(row = 0,
                                rowspan = 11,
                                column = 1,
                                columnspan = 1,
                                padx = PADX,
                                pady = PADY,
                                sticky = "nsew"
                                )

        # checks if any variables were updated
        self.sys_files_var.trace_add("write", self.update_tree)
        self.cwd_var.trace_add("write", self.update_tree)

        # save the current config
        self.after(100, self.save_recent)

        # hotkeys and their functionality
        self.bind("<Control-g>", self.goto)

    def goto(self, event) -> None: # pylint: disable=unused-argument
        """
        Creates a popup allowing the user to view a path.
        """

        self.goto_popup = GotoPopup(self.font)

        try:
            path = self.goto_popup.get_input()
            path = expanduser(path)

            # only view the path in the explorer if the path is valid
            if path is not None and path != "":
                if isfile(path): # if the path is a file
                    dir_path = dirname(path)
                    self.cwd_var.set(dir_path)
                else: # a directory
                    self.cwd_var.set(path)

        except PermissionError:
            WarnBox(f"{SCRIPT_DIR}/source/misc/warning.png",
                    "Error: This is a system\nfile or directory and cannot\nbe viewed.",
                    self.font
                    )

    def quit_app(self) -> None:
        """
        Quits the application.
        """

        self.destroy()
        sys_exit(0)

    def update_tree(self, *args) -> None: # pylint: disable=unused-argument
        """
        Updates the file explorer tree from the app itself. Could be done with 
        app.file_explorer.fill_tree, but this is a lot cleaner and easier to read.
        """

        self.file_explorer.fill_tree(self.cwd_var.get(),
                                     self.sys_files_var.get(),
                                     )

        # clear previous path text widget
        self.path_text.destroy()

        # path text (breadcrumbs) widgets
        self.path_text = PathLabel(self,
                                   self.cwd_var.get(),
                                   font = self.font
                                   )

        self.path_text.grid(row = 11,
                            column = 1,
                            padx = PADX,
                            pady = PADY,
                            sticky = "sw"
                            )

        self.save_recent()

    def open_recent(self) -> None:
        """
        Opens the configuration file with the most recent user settings.
        """

        if exists(CONFIG_PATH) and exists(CONFIG_PATH.removesuffix("/settings.cfg")):
            with open(CONFIG_PATH, "r", encoding = "utf-8") as config_file:
                settings = load(config_file)

                self.cwd_var.set(settings["cwd"])
                self.sys_files_var.set(settings["sys_files"])

                ctk.set_appearance_mode(settings["appearance_mode"].lower())

                self.scale_percent = settings["ui_scale"]
                scale_float = int(self.scale_percent.replace("%", "")) / 100
                ctk.set_widget_scaling(scale_float)

                self.theme_name = settings["theme"]
                if " " in self.theme_name:
                    no_spaces_theme = self.theme_name.replace(" ", "_")
                else:
                    no_spaces_theme = self.theme_name

                self.font_name = settings["font"]
                if " " in self.font_name:
                    no_spaces_font = self.font_name.replace(" ", "_")
                else:
                    no_spaces_font = self.font_name

                ctk.set_default_color_theme(f"{THEME_PATH}/{no_spaces_theme.lower()}.json")
                ctk.FontManager.load_font(f"{FONT_PATH}/{no_spaces_font.lower()}.ttf")

                size = (settings["width"], settings["height"])
                self.geometry(f"{size[0]}x{size[1]}")

                config_file.close()

        else:
            ctk.set_appearance_mode("system")
            ctk.set_default_color_theme(f"{THEME_PATH}/default.json")
            ctk.FontManager.load_font(f"{FONT_PATH}/dm_mono.ttf")

            self.theme_name = "Default"
            self.font_name =  "DM Mono"
            self.scale_percent = "100%"

        if ctk.get_appearance_mode().lower() == "light":
            icon_image = Image.open(LIGHT_ICON_PATH)
            self.iconphoto(True, ImageTk.PhotoImage(icon_image))
        elif ctk.get_appearance_mode().lower() == "dark":
            icon_image = Image.open(DARK_ICON_PATH)
            self.iconphoto(True, ImageTk.PhotoImage(icon_image))

    def save_recent(self) -> None:
        """
        Saves the most recent settings to a file. These settings include the current directory,
        theme, and the system files toggle.
        """

        if not exists(CONFIG_PATH.removesuffix("/settings.cfg")):
            mkdir(CONFIG_PATH.removesuffix("/settings.cfg"))

        with open(CONFIG_PATH, "w", encoding = "utf-8") as config_file:
            settings = {"cwd": self.cwd_var.get(),
                        "sys_files": self.sys_files_var.get(),
                        "appearance_mode": self.appearance_menu.get(),
                        "theme": self.theme_menu.get(),
                        "ui_scale": self.scale_menu.get(),
                        "width": self.winfo_width(),
                        "height": self.winfo_height(),
                        "font": self.font_menu.get()
                        }

            dump(settings, config_file)
            config_file.close()

# create and run the app
if __name__ == "__main__":
    hive_app = HiveApp()
    hive_app.mainloop()
