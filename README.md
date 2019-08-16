# vscode-extensions

Scripts to install my extensions for Visual Studio Code

## Getting started

1) Launch your **Linux terminal** or **Windows command line** program

2) Go to the project folder : `cd "project_folder_path/vscode-extensions"`

## Install extensions script

### Commands

Get help : `python vscode.py -h`

```bash
usage: vscode.py [-h] [-i] [-c] [-ri] [-ui] [-o] [-k KEYBINDINGS_FOLDER_PATH]
                 [-s SETTINGS_FOLDER_PATH]

optional arguments:
  -h, --help            show this help message and exit
  -i, --install         Install only extra extensions
  -c, --copy            Overright extensions in the list with yours
  -ri, --re-install     Reinstall all your extensions
  -ui, --un-install-all
                        Uninstall all your extensions
  -o, --revert-operation
                        To go back from operation install or reinstall (keep
                        only your previous extensions)
  -k KEYBINDINGS_FOLDER_PATH, --set-keys KEYBINDINGS_FOLDER_PATH
                        Set your shortcuts to the keybindings.json in
                        vscodeFiles
  -s SETTINGS_FOLDER_PATH, --set-settings SETTINGS_FOLDER_PATH
                        Set your settings to the settings.json in vscodeFiles
```

Install only extra extensions : `python vscode.py --install`

Overright extensions in the list with yours : `python vscode.py --copy`

Reinstall all your extensions : `python vscode.py --re-install`

Uninstall all your extensions : `python vscode.py --un-install-all`

To go back from operation install or reinstall (keep only your previous extensions) :

`python vscode.py --revert-operation`

Set your shortcuts to the keybindings.json in vscodeFiles :

`python vscode.py --set-keys "KEYBINDINGS_FOLDER_PATH"`

Set your shortcuts to the settings.json in vscodeFiles :

`python vscode.py --set-keys "SETTINGS_FOLDER_PATH"`

default vscode user folder path are :
Windows : %APPDATA%\\Code\\User\\
Linux : $HOME/.config/Code/User/
Mac : $HOME/Library/Application Support/Code/User/

### Finally

When it's completed restart **Visual Studio Code**

## Use Case

1) I need to deploy a vscode environnement on multiple computers

2) When I change companies I want to have my preconfigured environnement and be operationnal faster

3) I want the same environnement on all my computers
