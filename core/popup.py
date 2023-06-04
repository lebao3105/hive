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

from PIL import Image

import customtkinter as ctk
from .config import *

class Popup(ctk.CTkToplevel):
    def __init__(self, icon_path: str, message: str, font: tuple) -> None:
        """
        A window that displays a message instructing the user to restart the app after selecting a
        new theme.
        """

        # setup widget
        super().__init__()
        self.title("restart")
        self.geometry("250x150")
        self.resizable(False, False)
        self.rowconfigure(0, weight = 1)
        self.rowconfigure(1, weight = 1)
        self.columnconfigure(0, weight = 1)

        # the popup image/icon
        icon = ctk.CTkImage(light_image = Image.open(f"{icon_path}popup.png"),
                            size = (55, 55)
                            )
        button = ctk.CTkButton(master = self,
                               image = icon,
                               text = "",
                               width = icon.cget("size")[0]
                               )
        button.grid(row = 0, column = 0, padx = PADX, pady = PADY)

        # create a text widget
        warning = PopupLabel(self, message, font)
        warning.grid(row = 1, column = 0, padx = PADX, pady = PADY)

class PopupLabel(ctk.CTkLabel):
    def __init__(self, master: ctk.CTk, message: str, font: tuple) -> None:
        """
        The text that goes inside the popup window.
        """

        # widget setup
        super().__init__(master = master,
                         text = f"Popup: {message}",
                         font = font
                         )
