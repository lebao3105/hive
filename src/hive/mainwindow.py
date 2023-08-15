# 	A whole new file explorer.
# 	Copyright (C) 2023 Le Bao Nguyen and contributors.
# 	Licensed under the GNU General Public License version 3.0 or later.

import os
import wx
import wx.xrc

from libtextworker.general import CraftItems
from libtextworker.interface.wx.miscs import XMLBuilder, BindMenuEvents

from .consts import CURRDIR, DATADIR
from .dialogs import AboutHive, ShowShortcuts, ShowSysSpecs
from .notebook import Notebook


class Window(XMLBuilder):
    """
    Main Hive class.
    """

    def __init__(self):
        XMLBuilder.__init__(self, None, CraftItems(DATADIR, "window.xrc"))

        # get what we need
        self.mainFrame: wx.Frame = self.loadObject("MainWindow", "wxFrame")
        self.toolbar: wx.ToolBar = wx.xrc.XRCCTRL(
            self.mainFrame, "AppToolbar", "wxToolBar"
        )
        self.mainFrame.SetSize((860, 640))  # from textworker

        # make aliases
        self.Show = self.mainFrame.Show
        self.Hide = self.mainFrame.Hide
        self.Close = self.mainFrame.Close

        # construct objects
        mainBoxer: wx.BoxSizer = self.mainFrame.GetSizer()
        splitBox = wx.SplitterWindow(self.mainFrame)

        self.leftDir = wx.GenericDirCtrl(
            splitBox, dir=CURRDIR, style=wx.DIRCTRL_DIR_ONLY | wx.DIRCTRL_EDIT_LABELS | wx.DIRCTRL_MULTIPLE
        )
        self.notebook = Notebook(splitBox)

        splitBox.SplitVertically(self.leftDir, self.notebook, 246)
        mainBoxer.Add(splitBox, 1, wx.GROW, 5)

        # bind events
        self.BindMenu()
        # self.BindToolbar()

        self.leftDir.GetTreeCtrl().Bind(
            wx.EVT_TREE_ITEM_ACTIVATED,
            lambda evt: (
                self.notebook.GetCurrentPage().GoDir(path=self.leftDir.GetPath())
            ),
        )

        # layout the frame
        self.mainFrame.Layout()
        self.mainFrame.Centre()

    def BindMenu(self):
        # Get all menus first
        filemenu = self.mainFrame.GetMenuBar().GetMenu(0)
        navmenu = self.mainFrame.GetMenuBar().GetMenu(1)
        helpmenu = self.mainFrame.GetMenuBar().GetMenu(2)

        # Events list
        filemenu_events = [
            (self.NewWindow, 0),
            # Undo: not available
            # Redo: not available
            # Settings: not available
            (lambda evt: wx.GetApp().ExitMainLoop(), 4)
        ]

        navmenu_events = [
            (self.GoTo, 0),
            (self.notebook.GetCurrentPage().GoUp, 1),
            (self.notebook.NewTab, 4)
        ]

        helpmenu_events = [
            (lambda evt: ShowShortcuts(self.mainFrame), 0),
            (AboutHive(self.mainFrame).ShowBox, 1),
            (lambda evt: ShowSysSpecs(self.mainFrame), 2),
        ]

        BindMenuEvents(self.mainFrame, filemenu, filemenu_events)
        BindMenuEvents(self.mainFrame, navmenu, navmenu_events)
        BindMenuEvents(self.mainFrame, helpmenu, helpmenu_events)

    def NewWindow(self, evt):
        new = Window()
        wx.GetApp().SetTopWindow(new.mainFrame)
        new.mainFrame.Bind(wx.EVT_CLOSE, lambda evt: (wx.GetApp().SetTopWindow(self.mainFrame), evt.Skip()))
        new.Show()
    
    def GoTo(self, evt):
        dlg = wx.TextEntryDialog(self.mainFrame, "", "Go to")
        if dlg.ShowModal() == wx.ID_OK:
            value = os.path.expanduser(dlg.GetValue())
            if not os.path.isdir(value):
                wx.MessageBox(f"Directory not found: {value}")
                return
            self.notebook.GetCurrentPage().GoDir(path=value)