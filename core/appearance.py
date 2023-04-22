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

import customtkinter as ctk

class AppearanceLabel(ctk.CTkLabel):
    def __init__(self, master: ctk.CTk):
        """
        Widget that explains what the menu below it is for/does.
        """

        # widget setup
        super().__init__(master = master,
                         text = "Appearance"
                         )

class AppearanceSelector(ctk.CTkOptionMenu):
    def __init__(self, master: ctk.CTk):
        """
        Widget that allows the user to select a theme from light, dark, or system default.
        """

        # widget setup
        super().__init__(master = master,
                         values = ["System", "Light", "Dark"],
                         command = self.change_appearance,
                         )

    def change_appearance(self, new_appearance: str):
        """
        Changes the appearance/theme of the app.

        Args:
            new_appearance (str): The new appearance/theme. Either "System", "Light", or "Dark".
        """
        ctk.set_appearance_mode(new_appearance.lower())
