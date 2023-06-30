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

class GotoPopup(ctk.CTkInputDialog):
    def __init__(self, font: tuple) -> None: # pylint: disable=unused-argument
        """
        A window that allows users to view a specific path.
        """

        # widget setup
        super().__init__(title = "go to",
                         text = "View any path in the file explorer:",
                         # font = font
                         )
