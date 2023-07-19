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

from .const import *

from .helper import *

from .appearance import AppearanceLabel, AppearanceMenu

from .file_explorer import FileExplorer

from .path_text import PathLabel

from .sys_files import SysFilesLabel, SysFilesSwitch

from .theme import ThemeLabel, ThemeMenu

from .popup import *

from .ui_scale import ScaleLabel, ScaleMenu

from .rename import RenamePopup

from .font import FontMenu

from .info import InfoPopup

from .trash import TrashButton
