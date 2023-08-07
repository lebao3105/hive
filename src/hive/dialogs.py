#	A whole new file explorer.
#	Copyright (C) 2023 Le Bao Nguyen and contributors.
#	Licensed under the GNU General Public License version 3.0 or later.

import platform
import wx

from libtextworker import __version__ as libver
from libtextworker.general import CraftItems
from libtextworker.interface.wx.about import AboutDialog
from libtextworker.interface.wx.miscs import XMLBuilder

from .consts import DATADIR, VERSION as appver, ARTISTS, DEVELOPERS, DOCWRITERS

class AboutHive(AboutDialog):
    """
    About dialog of Hive program.
    """

    def __init__(self, parent: wx.Window | None = None):
        self.Parent = parent
        self.SetArtists(ARTISTS)
        self.SetCopyright("(C) 2023 Le Bao Nguyen, Dishant B and contributors.")
        self.SetDescription("A whole new file explorer!")
        self.SetDevelopers(DEVELOPERS)
        self.SetDocWriters(DOCWRITERS)
        self.SetLicense("GPL3_short", True)
        self.SetName("Hive")
        self.SetVersion(appver)
        self.SetWebSite("https://github.com/lebao3105/hive")

def ShowSysSpecs(parent: wx.Window):
    """
    Show system specifications dialog:
    * libtextworker verison
    * wx version (including wxPython)
    * OS arch + version
    Good for debugging, I guess?
    """

    dlg = wx.Dialog(parent, title="System specifications")
    label = wx.StaticText(dlg)
    label.SetLabelText(
        f"""
        Using:
        libtextworker {libver}
        wxPython {wx.version()}
        OS: {platform.system()} {platform.version()} on {platform.architecture()} architecture
        For the app version, please check the About dialog.
        """
    )
    dlg.ShowModal()

def ShowShortcuts(parent: wx.Window):
    """
    Show Shortcuts window
    """

    dlg = wx.Dialog(parent, title=_("Shortcuts"))
    builder = XMLBuilder(dlg, CraftItems(DATADIR, "shortcuts.xrc"), _)
    builder.loadObject("MyPanel1", "wxPanel")
    dlg.ShowModal()