# 	A whole new file explorer.
# 	Copyright (C) 2023 Le Bao Nguyen and contributors.
# 	Licensed under the GNU General Public License version 3.0 or later.

from os.path import expanduser
from libtextworker import THEMES_DIR, TOPLV_DIR
from libtextworker.general import WalkCreation
from libtextworker.versioning import require
from libtextworker._importer import test_import

test_import("wx")
THEMES_DIR = expanduser("~/.hive/themes")
TOPLV_DIR = expanduser("~/.hive")
WalkCreation(THEMES_DIR)
require("libtextworker", "0.1.4")
