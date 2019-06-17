#!/usr/bin/env python

import os
import sys


extensions_file = "vscodeExtensionsList.txt"


def create_my_extensions_file():
    """
    Create a file with current installed extensions
    """

    os.system("code --list-extensions > " + "myPrevousExtentions.txt") 


def compare(file_compared,file_master):
    """
    Compare your extentions with the extension file
    To avoid delay if the extension is already installed
    A = [100,200,300] 
    B = [400,500,100]
    compare(A,B) = [200,300]
    """

    file_compared_extensions = []
    file_master_extensions = []

    with open(file_compared,'r') as fc:
        for line in fc:
            file_compared_extensions.append(line.strip())

    with open(file_master,'r') as fm:
        for line in fm:
            file_master_extensions.append(line.strip())

    return list(set(file_compared_extensions) - set(file_master_extensions))


def install_all_extensions(command,file_compared,file_master):
    different_extensions = compare(file_compared, file_master)

    for line in different_extensions:
        os.system(command + " " + line)


choose = input("Choose one :\n"+
                "(1) Install only extra extensions\n" +
                "(2) Overright extensions in the list with yours\n" +
                "(3) Reinstall all your extensions\n" +
                "(4) To go back from operation 2 (keep only your previous extensions)\n" +
                "(5) Exit\n" +
                ": ")

if choose == '1':
    create_my_extensions_file()
    install_all_extensions("code --install-extension", extensions_file, "myPrevousExtentions.txt")
elif choose == '2':
    os.system("code --list-extensions > " + extensions_file)
elif choose == '3':
    create_my_extensions_file()
    install_all_extensions("code --uninstall-extension", "myPrevousExtentions.txt", extensions_file)
    install_all_extensions("code --install-extension", extensions_file, "myPrevousExtentions.txt")
elif choose == '4':
    install_all_extensions("code --uninstall-extension", extensions_file, "myPrevousExtentions.txt")
    install_all_extensions("code --install-extension", "myPrevousExtentions.txt", extensions_file)
elif choose == '5':
    sys.exit()
else:
    print("Between 1 and 3")
    choose = input("Choose one :\n"+
                "(1) Install only extra extensions\n" +
                "(2) Reinstall all your extensions\n" +
                "(3) To go back from operation 2 (keep only your previous extensions)\n" +
                "(4) Exit\n" +
                ": ")


print("Installation Completed")