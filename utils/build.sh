#!/bin/sh

pyinstaller -i=./src/icons/dark.png -n=hive --log-level=WARN --clean --noconfirm --onedir --windowed --add-data "$HOME/Library/Python/3.9/lib/python/site-packages/customtkinter:customtkinter/"  "$HOME/Documents/hive/hive.py"
