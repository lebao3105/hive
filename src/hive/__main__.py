#	A whole new file explorer.
#	Copyright (C) 2023 Le Bao Nguyen and contributors.
#	Licensed under the GNU General Public License version 3.0 or later.

import argparse, wx
from . import consts

parser = argparse.ArgumentParser(description="A whole new file explorer.")
parser.add_argument(
    "folderpaths", type=str, nargs="?",
    help="Folders to open"
)
parser.add_argument(
    "--version", "-v", action="store_true",
    help="Show the app version and exit"
)

if __name__ == "__main__":
    args = parser.parse_args()
    app = wx.App()

    from . import mainwindow
    mw = mainwindow.Window()

    if args.version:
        print(consts.VERSION)
        exit(0)

    if args.folderpaths:
        consts.CURRDIR = parser.folderpaths

    mw.notebook.NewTab(path=consts.CURRDIR)
    mw.Show()
    app.MainLoop()