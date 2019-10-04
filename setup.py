#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

# Deploys the project using the serverless framework to AWS lambda
# os.system("cd ~/WKS/src/gitlab.com/moonshotlabs/mylegal && make clean && make deploydev")

# Setup my Visual Studio Code
os.system("python vscode.py -k /home/developer/.config/Code/User/")
os.system("python vscode.py -s /home/developer/.config/Code/User/")
print("\n")
os.system("python vscode.py --install")

# Go back to main project
os.system("code ~/WKS/src/gitlab.com/moonshotlabs/mylegal")

print("\nEnvironnement setup COMPLETED")
