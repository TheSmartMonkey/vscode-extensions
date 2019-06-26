# vscode-extensions

Scripts to install my extensions for Visual Studio Code

## Getting started

1) Launch your **Linux terminal** or **Windows command line** program

2) Install argparse python module : `pip install argparse`

3) Go to the project folder : `cd "project_folder_path/vscode-extensions"`

## Install extensions script

### Commands

Get help : `python vscodeExtensions.py -h`

```bash
optional arguments:
  -h, --help            show this help message and exit
  -i, --install         Install only extra extensions
  -c, --copy            Overright extensions in the list with yours
  -ri, --re-install     Reinstall all your extensions
  -ro, --revert-operation
                        To go back from operation install or reinstall (keep
                        only your previous extensions)
```

Install only extra extensions : `python vscodeExtensions.py --install`

Overright extensions in the list with yours : `python vscodeExtensions.py --copy`

Reinstall all your extensions : `python vscodeExtensions.py --re-install`

To go back from operation install or reinstall (keep only your previous extensions) : 

`python vscodeExtensions.py --revert-operation`

### Finally

When it's completed restart **Visual Studio Code**

## Use Case

1) I need to deploy a vscode environnement on multiple computers

2) When I change companies I want to have my preconfigured environnement and be operationnal faster

3) I want the same environnement on all my computers
