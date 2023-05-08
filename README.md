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
    <h1>hive</h1>
    A whole new file explorer for macOS. Finder, but better.
</div>

## About:
In its current state, `hive` is a simple file explorer for macOS. It has a clean, modern, and simple user-interface as well as light and dark modes. In `hive`, you can toggle system files (which are usually hidden), open files (or apps), and navigate through directories/folders. The path to the directory you are viewing is displayed at the bottom of the window.

## Download:
You can find the most recent build in the [Releases section](https://github.com/dishb/hive/releases) of this repository. Each release contains details as well as a version number.

## Build:
If you want to build `hive` from source yourself, follow the commands and instructions listed below.

If you haven't already, install the latest version of Python from the [official website](https://python.org/downloads/).
```bash
# create a dir for the repo, change to it
mkdir $HOME/Documents/hive/
cd $HOME/Documents/hive/

# clone this repo
git clone https://github.com/dishb/hive.git .

# make sure pip is updated
pip3 install --upgrade pip

# install all the dependencies
pip3 install --upgrade pyinstaller
pip3 install --upgrade customtkinter
pip3 install --upgrade pillow

# run the build script
python3 ./utility/build.py
```
The build can be found in the `./dist/` folder. It will be a macOS application with the name `hive.app`.

## Security:
If you find a security issue or vulnerability, please follow the instructions listed [here](./SECURITY.md) on in the `./SECURITY.md`  file.

## Code of Conduct:
To keep this repository friendly and open to everyone, please ensure that you follow the guidelines [here](./CODE_OF_CONDUCT.md) or in the `./CODE_OF_CONDUCT.md` file.

## License:
This project is licensed under the `GNU General Public Lesser v3` license. A copy of the license can be found in [here](./LICENSE.md) or in the `./LICENSE.md` file. All the source code files have a license header at the top.
