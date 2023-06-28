<!--
    A whole new file explorer for macOS. Finder, but better.
    Copyright (C) 2023  Dishant B. (@dishb) <code.dishb@gmail.com> and contributors.

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
-->

<div align = 'center'>
    <h1>Files and Folders</h1>
    This document details what each file and folder's purpose is in the repository.
</div>

## Folders:
Folders are also referred to as "directories".
- `./github/`: Where the Github workflow files are stored.
- `./core/`: All the widgets and classes that `hive` uses. Most of the code can be found here.
- `./images/`: Screenshots of `hive`. This is used for showcasing the application in the `README.md` file.
- `./source/`: Resources that `hive` uses. This includes icons, images, fonts, and themes (as `.json` files).
- `./utility/`: Scripts for `hive`'s developers. This includes a Python script to build `hive` into a bundled application/
- `./.gitignore`: Tells Git to not include specific files or directories when making commits.
- `.pylintrc`: A file that configures `pylint` through available options. Some options include ignoring specific files.
- `./hive.py`: The main code/file. If you want to run `hive.py` from source, you'll want to run this file.
- `./requirements.txt`: A list of all of `hive`'s dependencies.
