#	A whole new file explorer.
#	Copyright (C) 2023 Le Bao Nguyen and contributors.
#	Licensed under the GNU General Public License version 3.0 or later.

import os
import wx
import wx.xrc

from libtextworker._importer import test_import
test_import("wx")
from libtextworker.general import CraftItems
from libtextworker.interface.wx.miscs import XMLBuilder, BindMenuEvents


from .consts import DATADIR
from .dialogs import AboutHive, ShowSysSpecs
from .notebook import Notebook

class Window(XMLBuilder):
    """
    Main Hive class.
    """

    def __init__(self):
        XMLBuilder.__init__(
            self,
            None,
            CraftItems(DATADIR, "window.xrc")
        )

        self.mainFrame: wx.Frame = self.loadObject("MainWindow", "wxFrame")
        self.toolbar: wx.ToolBar = wx.xrc.XRCCTRL(self.mainFrame, "AppToolbar", "wxToolBar")

        self.mainFrame.SetSize((860, 640)) # from textworker
        self.Show = self.mainFrame.Show
        self.Hide = self.mainFrame.Hide
        self.Close = self.mainFrame.Close

        mainBoxer: wx.BoxSizer = self.mainFrame.GetSizer()
        self.notebook = Notebook(self.mainFrame)
        mainBoxer.Add(self.notebook, 1, wx.GROW, 5)

        self.BindMenu()
        # self.BindToolbar()
        self.mainFrame.Layout()
        self.mainFrame.Centre()
    
    def BindMenu(self):

        # Get all menus first
        filemenu = self.mainFrame.GetMenuBar().GetMenu(0)
        navmenu = self.mainFrame.GetMenuBar().GetMenu(1)
        helpmenu = self.mainFrame.GetMenuBar().GetMenu(2)

        # Events list
        filemenu_events = [
            # Undo: not available
            # Redo: not available
            # Settings: not available
            (wx.GetApp().ExitMainLoop(), 3)
        ]

        helpmenu_events = [
            # Shortcuts is not available
            (AboutHive(self.mainFrame).ShowBox, 1),
            (lambda evt: ShowSysSpecs(self.mainFrame), 2)
        ]

        BindMenuEvents(self.mainFrame, filemenu, filemenu_events)
        BindMenuEvents(self.mainFrame, helpmenu, helpmenu_events)