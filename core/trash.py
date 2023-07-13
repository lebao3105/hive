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

from .config import USER

class TrashButton(ctk.CTkButton):
    def __init__(self, master: ctk.CTk, icon_path: str, font: tuple) -> None:
        """
        A button allowing a user to view their trash.
        """

        # attributes
        self.icon_path = icon_path
        self.master = master
        self.icon = ctk.CTkImage(light_image = Image.open(f"{self.icon_path}trash.png"))

        # widget setup
        super().__init__(master = self.master,
                         text = "Trash",
                         image = self.icon,
                         font = font,
                         command = self.view_trash
                         )

    def view_trash(self) -> None:
        """
        Views the user's trash in the file explorer.
        """

        self.master.cwd_var.set(f"/Users/{USER}/.Trash")
