#!/usr/bin/env python

import os


extensions_file = "vscodeExtensionsList.txt"


def create_extensions_file(my_extension_file):
    """
    Create a file with current installed extensions
    """

    os.system("code --list-extensions > " + my_extension_file) 


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


if __name__ == '__main__':
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument('-i', '--install', default = 'install', help = 'Install only extra extensions', action = 'store_true', dest = "install")
    parser.add_argument('-c', '--copy', default = 'copy', help = 'Overright extensions in the list with yours', action = 'store_true', dest = "copy")
    parser.add_argument('-ri', '--re-install', default = 'reinstall', help = 'Reinstall all your extensions', action = 'store_true', dest = "reinstall")
    parser.add_argument('-ro', '--revert-operation', default = 'revert', help = 'To go back from operation install or reinstall (keep only your previous extensions)', action = 'store_true', dest = "revert")
    arguments = parser.parse_args()

    # Install only extra extensions
    if arguments.install is True:
        create_extensions_file("myPrevousExtentions.txt")
        install_all_extensions("code --install-extension", extensions_file, "myPrevousExtentions.txt")
        print("\nInstallation COMPLETED")

    # Overright extensions in the list with yours
    if arguments.copy is True:
        file_previous_extensions = []
        file_final_extensions = []

        with open(extensions_file,'r') as fp:
            for line in fp:
                file_previous_extensions.append(line.strip())

        create_extensions_file(extensions_file)

        with open(extensions_file,'r') as ff:
            for line in ff:
                file_final_extensions.append(line.strip())

        # Print extensions that have been added to the vscodeExtensionsList.txt file
        added_extensions = list(set(file_final_extensions) - set(file_previous_extensions))
        removed_extensions = list(set(file_previous_extensions) - set(file_final_extensions))

        if len(added_extensions) > 0:
            print("\nAdded Extensions in file:")
            for extensions in added_extensions:
                print(extensions)

        if len(removed_extensions) > 0:
            print("\nRemoved Extensions in file:")
            for extensions in removed_extensions:
                print(extensions)

        print("\nCopy extensions in file COMPLETED")

    # Reinstall all your extensions
    if arguments.reinstall is True:
        create_extensions_file("myPrevousExtentions.txt")
        install_all_extensions("code --uninstall-extension", "myPrevousExtentions.txt", extensions_file)
        install_all_extensions("code --install-extension", extensions_file, "myPrevousExtentions.txt")
        print("\nReinstallation COMPLETED")

    # To go back from operation install or reinstall (keep only your previous extensions)
    if arguments.revert is True:
        install_all_extensions("code --uninstall-extension", extensions_file, "myPrevousExtentions.txt")
        install_all_extensions("code --install-extension", "myPrevousExtentions.txt", extensions_file)
        print("\nRevert operation COMPLETED")
