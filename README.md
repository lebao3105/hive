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

## About:
`hive` is a file explorer for macOS. At its core, `hive` is pure Python and uses the `customtkinter` module. This project is meant to be a simple file explorer with a clean and modern UI. While it's not as good as Finder yet, `hive` is meant to be a replacement for the somewhat dull, complex Finder. Users will be able to do everything they can in Finder, just without the clutter and extra nonsense. `hive` is targeted at casual users. People who don't need to harvest the full power of the operating system and file system. 

By being open source, `hive` can establish a community of users that can help contribute to the project through code, documentation, and more. The community can look at the internal workings of this tool and find potential issues. Suggestions can be made and development sped up. Open source allows this project to have a much higher chance of surviving and not dying out.

## Images:
You can find screenshots of `hive` in the `./images` folder or [here](https://github.com/dishb/hive/tree/20da48fb7e18305743c7e491de8ad361a919d252/images).

## Customization
While `hive` already has many options for customizing the theme, you can still add your own themes and fonts! For themes, just drop the `.json` file into the `~/.hive/themes/` directory. For fonts, drop the `.ttf` file into the `~/.hive/fonts/` directory. In `hive`, you can select your new theme and font!

## Download:
You can find the most recent build in the [Releases section](https://github.com/dishb/hive/releases) of this repository. Each release contains details as well as a version number.

## Getting started:
To get started with `hive` whether it be developing, building, or just normal usage, you'll need to follow the commands and instructions below:
```bash
# create a folder for the repo, clone it
git clone https://github.com/dishb/hive
cd ./hive/

# create a virtual environment and activiate it
python3 -m venv ./venv/
source ./venv/bin/activate

# upgrade pip and install dependencies
pip3 install --upgrade pip
pip3 install -r requirements.txt
```

## Run:
If you want to run `hive` from source, first read the [Getting started](#getting-started) section, then run this command:
```bash
python3 ./hive.py
```

## Build:
If you want to build `hive` from source yourself, first read the [Getting started](#getting-started) section, then run this command:
```bash
python3 ./utility/build.py
```
The build will be found in the `./dist/` folder with the name `hive.app`.

## Contributing:
If you want to contribute, please read the cotributing guide [here](./CONTRIBUTING.md) or in the `./CONTRIBUTING.md` file.

## Files and Folders:
If you're confused on what each file and/or directory in this repository is for, details can be found in `./FILES.md` or [here](./FILES.md).

## Security:
If you find a security issue or vulnerability, please follow the instructions listed [here](./SECURITY.md) on in the `./SECURITY.md`  file.

## Code of Conduct:
To keep this repository friendly and open to everyone, please ensure that you follow the guidelines [here](./CODE_OF_CONDUCT.md) or in the `./CODE_OF_CONDUCT.md` file.

## License:
This project is licensed under the `GNU General Public License v3` license. A copy of the license can be found in [here](./LICENSE.md) or in the `./LICENSE.md` file. All the source code files have a license header at the top.

## Credits:
`hive` and its development would not have been possible without these open-source projects:
- [Python](https://github.com/python/cpython/) (yes, the language!)
- [customtkinter](https://github.com/TomSchimansky/CustomTkinter)
- [Pillow](https://github.com/python-pillow/Pillow)
- [CTkXYFrame](https://github.com/Akascape/CTkXYFrame)
- [pyinstaller](https://github.com/pyinstaller/pyinstaller/)
- [pylint](https://github.com/pylint-dev/pylint)
