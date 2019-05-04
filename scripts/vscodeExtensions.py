#!/usr/bin/env python

import os

extensions_file = "vscodeExtensionsList.txt"

with open(extensions_file,"r") as f:
    for line in f:
        os.system("code --install-extension " + line)

print("Installation Completed")