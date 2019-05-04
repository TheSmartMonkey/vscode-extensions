#!/usr/bin/env python

import os

extensions_file = "vscodeExtensionsList.txt"

os.system("code --list-extensions > " + extensions_file)