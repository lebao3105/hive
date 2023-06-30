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

from .config import SCRIPT_DIR, THEME_PATH
from .popup import Popup
from .helper import get_all_themes

class ThemeLabel(ctk.CTkLabel):
    def __init__(self, master: ctk.CTk, font: tuple) -> None:
        """
        Widget that explains what the menu below it is for/does.
        """

        # widget setup
        super().__init__(master,
                         text = "Theme:",
                         font = font
                         )

class ThemeMenu(ctk.CTkOptionMenu):
    def __init__(self, master: ctk.CTk, font: tuple) -> None:
        """
        Widget that allows the user to select a theme from several options.
        """

        # font setup
        self.font = font

        # widget setup
        self.master = master
        self.options = get_all_themes(f"{SCRIPT_DIR}/source/themes/")
        super().__init__(self.master,
                         values = self.options,
                         command = self.change_theme,
                         font = self.font
                         )

    def change_theme(self, new_theme: str) -> None:
        """
        Changes the theme of the app.
        """

        Popup(f"{SCRIPT_DIR}/source/misc/popup.png",
              "Popup: Please restart\nfor changes to the\ntheme to take effect.",
              self.font
              )

        if " " in new_theme:
            new_theme = new_theme.replace(" ", "_")

        ctk.set_default_color_theme(f"{THEME_PATH}/{new_theme.lower()}.json")

        self.master.save_recent()
