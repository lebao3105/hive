#	A whole new file explorer.
#	Copyright (C) 2023 Le Bao Nguyen and contributors.
#	Licensed under the GNU General Public License version 3.0 or later.

import os
import wx
import wx.lib.agw.flatnotebook as FLB
from libtextworker.interface.wx.dirctrl import DirList, imgs, folderidx

class Notebook(FLB.FlatNotebook):
    """
    wxFlatNotebook with more flags enabled by default +
        forked AddPage.
    """
    
    def __init__(
        self,
        parent: wx.Window | None = None,
        id = wx.ID_ANY,
        pos: wx.Point = wx.DefaultPosition,
        size: wx.Point = wx.DefaultSize
    ):

        # Custom styles
        # Their name say everything they do
        styles = \
            FLB.FNB_ALLOW_FOREIGN_DND | \
            FLB.FNB_DEFAULT_STYLE | \
            FLB.FNB_HIDE_ON_SINGLE_TAB | \
            FLB.FNB_NAV_BUTTONS_WHEN_NEEDED
        
        FLB.FlatNotebook.__init__(self, parent, id, pos, size, agwStyle=styles)
        self.AssignImageList(imgs)
        self.Bind(FLB.EVT_FLATNOTEBOOK_PAGE_CLOSED, self.OnPageClosed)
    
    def NewTab(self, evt: wx.Event | None = None, path: str = os.path.expanduser("~/")):
        """
        Whatever create a new tab.
        """
        self.Freeze()
        new = DirList(self)
        new.DrawItems(path)

        self.AddPage(new, path, True, folderidx)
        self.Thaw()
    
    def OnPageClosed(self, evt):
        if self.GetPageCount() == 0:
            wx.GetApp().ExitMainLoop() # quit the app
        else:
            evt.Skip()
