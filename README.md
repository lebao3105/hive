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

## Build:
First, install the dependencies for `hive`.
```bash
pip3 install --upgrade pillow
pip3 install --upgrade customtkinter
```

Next, follow the commands listed below to build from source. The comments explain what they do.
```bash
cd $HOME/Documents/ # changes to your Documents directory
git clone https://github.com/dishb/hive.git . # clones the repo

cd ./hive/ # changes to the repo directory

chmod +x ./utils/build.sh # makes build script executable
./utils/build.sh # executes build script
```

The macOS application should be inside the `./dist/` directory. You can double click and run this app like any other.

## Download:
Find the most recent build in the [Releases section](https://github.com/dishb/hive/releases) of this repository. Each release contains details as well as a version number.

## Security:
If you find a security issue or vulnerability, please follow the instructions listed [here](./SECURITY.md) on in the `./SECURITY.md`  file.

## Code of Conduct:
To keep this repository friendly and open to everyone, please ensure that you follow the guidelines [here](./CODE_OF_CONDUCT.md) or in the `./CODE_OF_CONDUCT/md` file.

## License:
This project is licensed under the `GNU GPL v3` license. A copy of the license can be found in [here](./LICENSE.md) or in the `./LICENSE.md` file. All the source code files have a license header at the top.
