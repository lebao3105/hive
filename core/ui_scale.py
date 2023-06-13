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

class ScaleLabel(ctk.CTkLabel):
    def __init__(self, master: ctk.CTk, font: tuple) -> None:
        """
        A widget to explain what the menu under it is for.
        """

        super().__init__(master,
                         text = "UI Scaling:",
                         font = font
                         )

class ScaleMenu(ctk.CTkOptionMenu):
    def __init__(self, master: ctk.CTk, font: tuple) -> None:
        """
        A widget allowing the user to customize the scaling/size of the UI.
        """

        self.options = ["80%", "90%", "100%", "110%", "120%"]

        super().__init__(master,
                         values = self.options,
                         command = self.scale_ui,
                         font = font
                         )

        self.set("100%")

    def scale_ui(self, scale_percent: str) -> None:
        """
        Changes the UI scale of the widgets.
        """

        scale_float = int(scale_percent.replace("%", "")) / 100
        ctk.set_widget_scaling(scale_float)
