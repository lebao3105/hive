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
    <picture>
        <source media = "(prefers-color-scheme: dark)" srcset = "./source/icons/light.png">
        <source media = "(prefers-color-scheme: light)" srcset = "./source/icons/dark.png">
        <img alt = "hive's icon" src = "./source/icons/light.png" width = 300 height = 300>
    </picture>
    <h1>hive</h1>
    A whole new file explorer for macOS. Finder, but better.
</div>

> This version of Hive is died due to its structure. I really can't get used to it. A new version will be started later.

## About:
`hive` is a file explorer for macOS. At its core, `hive` is pure Python and uses the `customtkinter` module. This project is meant to be a simple file explorer with a clean and modern UI. While it's not as good as Finder yet, `hive` is meant to be a replacement for the somewhat dull, complex Finder. Users will be able to do everything they can in Finder, just without the clutter and extra nonsense. `hive` is targeted at casual users. People who don't need to harvest the full power of the operating system and file system. 

By being open source, `hive` can establish a community of users that can help contribute to the project through code, documentation, and more. The community can look at the internal workings of this tool and find potential issues. Suggestions can be made and development sped up. Open source allows this project to have a much higher chance of surviving and not dying out.

## Platforms:
As stated, `hive` is a file explorer for macOS. But this not means non-macOS users can't use it. A work for this is underway, and should be completed one day.

## Images:
You can find screenshots of `hive` in the [```./images```](./images/) folder.

## Customization
While `hive` already has many options for customizing the theme, you can still add your own themes and fonts! For themes, look for pre-made [themes](./source/themes/), make your own one, and drop the `.json` file into the `~/.hive/themes/` directory. For fonts, drop the `.ttf` file into the `~/.hive/fonts/` directory. In `hive`, you can select your new theme and font!

## Download:
You can find the most recent build in the [Releases section](https://github.com/dishb/hive/releases) of this repository. Each release contains details as well as a version number.

## Getting started:

Firstly, you will need the following:

* Python 3 with pip and Tkinter installed
* Git to clone this repository (optional)

To get started with `hive` whether it be developing, building, or just normal usage, you'll need to follow the commands and instructions below:

```bash
# create a folder for the repo, clone it
# or find and click the 'Download zip' button on GitHub page
git clone https://github.com/dishb/hive
cd ./hive/
git submodule update --init # get all Git submodules, will packed zip include this?

# create a virtual environment and activiate it
# you can skip it
python3 -m venv ./venv/
source ./venv/bin/activate

# upgrade pip and install dependencies
pip3 install --upgrade pip
pip3 install -r customtkinter
```

## Run:

If you want to run from source code:

```bash
python3 ./hive.py [folder]
```

Or make your own portable build, install ```pyinstaller``` with pip first, then run the following:

```bash
python3 ./utility/build.py build
python3 ./utility/build.py clean
```
The build will be found in the `./dist/` folder. Find and launch the executable.

# Shortcuts

* Space: Folder properties
* Ctrl + G: Go to path
* Middle click: Rename dialog

No cut-copy-paste(?).

No right-click.

## Contributing:
If you want to contribute, please read the contributing guide [here](./CONTRIBUTING.md) or in the `./CONTRIBUTING.md` file.

## Files and Folders:
If you're confused on what each file and/or directory in this repository is for, details can be found in `./FILES.md` or [here](./FILES.md).

## Security:
If you find a security issue or vulnerability, please follow the instructions listed [here](./SECURITY.md) on in the `./SECURITY.md`  file.

## Code of Conduct:
To keep this repository friendly and open to everyone, please ensure that you follow the guidelines [here](./CODE_OF_CONDUCT.md) or in the `./CODE_OF_CONDUCT.md` file.

## License:
This project is licensed under the `GNU General Public License v3` license. A copy of the license can be found in [here](./LICENSE.md). All the source code files have a license header at the top.

Source codes in [core/extensions](core/extensions/) are git submodules, and they are licensed by their author.

## Credits:
`hive` and its development would not have been possible without these open-source projects:
- [Python](https://python.org) (yes, the language!)
- [customtkinter](https://github.com/TomSchimansky/CustomTkinter)
- [Pillow](https://github.com/python-pillow/Pillow)
- [CTkXYFrame](https://github.com/Akascape/CTkXYFrame)
- [pyinstaller](https://github.com/pyinstaller/pyinstaller/)
- [pylint](https://github.com/pylint-dev/pylint)
