# vscode-extensions

Scripts to install my extensions, settings, keybindings for Visual Studio Code

## Getting started

1) Launch your **Linux terminal** or **Windows command line** or **Visual Studio Code terminal** program

2) Go to the project folder : `cd "project_folder_path/vscode-extensions"`

## Install extensions script

### Commands

Get help : `python vscode.py -h`

```bash
usage: vscode.py [-h] [-i] [-c] [-ri] [-ui] [-k KEYBINDINGS_FOLDER_PATH]
                 [-s SETTINGS_FOLDER_PATH] [-us USER_SNIPPETS_FOLDER_PATH]

optional arguments:
  -h, --help            show this help message and exit
  -i, --install         Install only extra extensions
  -c, --copy            Overright extensions in the extensionList.txt with
                        yours
  -ri, --re-install     Reinstall all your extensions
  -ui, --un-install-all
                        Uninstall all your extensions
  -k KEYBINDINGS_FOLDER_PATH, --set-keys KEYBINDINGS_FOLDER_PATH
                        Set your keys shortcuts to the keybindings.json in
                        vscodeFiles
  -s SETTINGS_FOLDER_PATH, --set-settings SETTINGS_FOLDER_PATH
                        Set your settings to the settings.json in vscodeFiles
  -us USER_SNIPPETS_FOLDER_PATH, --user-snippets USER_SNIPPETS_FOLDER_PATH
                        Set your snippets
```

* Install only extra extensions : `python vscode.py --install`

* Overright extensions in the extensionList.txt with yours : `python vscode.py --copy`

* Reinstall all your extensions : `python vscode.py --re-install`

* Uninstall all your extensions : `python vscode.py --un-install-all`

* Set your keys shortcuts to the keybindings.json in vscodeFiles : `python vscode.py --set-keys "KEYBINDINGS_FOLDER_PATH"`

* Set your settings to the settings.json in vscodeFiles : `python vscode.py --set-settings "SETTINGS_FOLDER_PATH"`

* Set your user snippets in the snippets folder : `python vscode.py --user-snippets "USER_SNIPPETS_FOLDER_PATH"`

Default vscode user folder path are :

**Windows** : `%APPDATA%\\Code\\User\\`

**Linux** : `$HOME/.config/Code/User/`

**Mac** : `$HOME/Library/Application Support/Code/User/`

### Finally

When it's completed restart **Visual Studio Code**

## Use Case

1) I need to deploy a vscode environnement on multiple computers

2) When I change companies I want to have my preconfigured environnement and be operationnal faster

3) I want the same environnement on all my computers
