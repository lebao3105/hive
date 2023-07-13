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

from .config import *

from .helper import *

from .appearance import AppearanceLabel
from .appearance import AppearanceMenu

from .file_explorer import FileExplorer

from .path_text import PathLabel

from .sys_files import SysFilesLabel
from .sys_files import SysFilesSwitch

from .theme import ThemeLabel
from .theme import ThemeMenu

from .warn_box import WarnBox

from .popup import Popup

from .ui_scale import ScaleLabel
from .ui_scale import ScaleMenu

from .rename import RenamePopup

from .goto import GotoPopup

from .font import FontMenu
from .font import FontLabel

from .info import InfoPopup

from .trash import TrashButton
