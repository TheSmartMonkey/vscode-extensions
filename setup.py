#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

# Deploys the project using the serverless framework to AWS lambda
os.system("cd ~/WKS/src/gitlab.com/moonshotlabs/mylegal")
os.system("make clean")
os.system("make deploy")

# Setup my Visual Studio Code
os.system("cd ~/vscode-extensions")
os.system("python vscode.py -k /home/developer/.config/Code/User/")
os.system("python vscode.py -s /home/developer/.config/Code/User/")
print("\n")
os.system("python vscode.py --install")

# Go back to main project
os.system("cd ~/WKS/src/gitlab.com/moonshotlabs/mylegal/ui")

print("\nSetup vscode COMPLETED")
