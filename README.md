## Hive

Hive, which is a "very new file explorer" like its expanded name.

Hive is a yet another file explorer, brings features like:

* Finder-like folder navigation
* Only a set of really-needed features are here, so this is not for advanced users who want to customize more & alot their interface (however I will bring some)
* Easy-to-config application interface: color, tree view, etc.

Color defines will be inherited from the legacy version (it's made for CustomTkinter btw, but there are useful values to be taken)

## Running

Requires Python 3.8+ with pip installed.

Since this project uses wxPython rather than Tkinter like the legacy version, you may need more dependencies.

As hive uses the unfinished libtextworker, so you probally need git.

Install attrdict3 first (for wxPython), then wxPython from pip.

To run from source code, cd to ```src``` and run:

```bash
$ # libtextworker can be installed - this is optional for now
$ # if installed you don't need to set PYTHONPATH
$ PYTHONPATH=<path_to_libtextworker> python3 -m hive
```

## Contribute

Contributions are welcomed here!

You can finish the Hive's [TODO](./TODO) list, or make your own cool features!

When you finish your work, you can make a PR for this repo.

## License

This project is licensed in GNU General Public License (GPL for short) version 3 or later, both the current and legacy one.

See [this file](./LICENSE) for the full license.