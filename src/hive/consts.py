#	A whole new file explorer.
#	Copyright (C) 2023 Le Bao Nguyen and contributors.
#	Licensed under the GNU General Public License version 3.0 or later.

import os
import platform
import wx

CURRDIR: str | list[str] = os.environ["USER" if platform.system() != "Windows" else "USERPROFILE"]
DATADIR: str = f"{os.path.dirname(__file__)}/../../data"
VERSION: str = "1.0"

# Credits
DEVELOPERS = DOCWRITERS = \
    [
        "Dishant B (@dishb on GitHub) - for the original Hive",
        "Le Bao Nguyen (@lebao3105 on GitHub) - the current Hive"
    ]

ARTISTS = \
    [
        "Dishant B for the app icon",
        "Le Bao Nguyen for app assets (tooltips etc)"
    ]