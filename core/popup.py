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

import customtkinter as ctk
from PIL import Image

from .const import PADX, PADY, SCRIPT_DIR

class Popup(ctk.CTkToplevel):
    """
    Base class for hive dialogs.
    """

    def __init__(self, icon_path: str, message: str, font: tuple, title: str) -> None:

        # basic TopLevel setups
        super().__init__()
        self.title(title)
        self.geometry("250x150")
        self.resizable(False, False)

        self.rowconfigure(0, weight = 1)
        self.rowconfigure(1, weight = 1)
        self.columnconfigure(0, weight = 1)

        # the popup image/icon
        self.icon = ctk.CTkImage(light_image = Image.open(icon_path),
                            size = (55, 55)
                            )
        button = ctk.CTkButton(master = self,
                               image = self.icon,
                               text = "",
                               width = self.icon.cget("size")[0]
                               )
        button.grid(row = 0,
                    column = 0,
                    padx = PADX,
                    pady = PADY
                    )

        # create a text widget
        warning = PopupLabel(self, message, font)
        warning.grid(row = 1,
                     column = 0,
                     padx = PADX,
                     pady = PADY
                     )

class PopupLabel(ctk.CTkLabel):
    def __init__(self, master: ctk.CTk, message: str, font: tuple) -> None:
        """
        The text that goes inside the popup window.
        """

        # widget setup
        super().__init__(master = master,
                         text = message,
                         font = font
                         )

def WarnBox(message: str, font: tuple):
    return Popup(f"{SCRIPT_DIR}/source/misc/warning.png", message, font, "Warning")

def ErrorBox(message: str, font: tuple):
    return Popup(f"{SCRIPT_DIR}/source/misc/error.png", message, font, "Error")

def InfoBox(message: str, font: tuple, title: str):
    return Popup(f"{SCRIPT_DIR}/source/misc/popup.png", message, font, title)