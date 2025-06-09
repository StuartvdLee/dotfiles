#!/usr/bin/env python

import os
import subprocess
import sys
import platform

def save_code_extensions(shell):
    """Save the list of installed VSCode extensions to ./VSCode/code_extensions"""
    print("Saving VSCode extensions…")
    with open("VSCode/code_extensions", "w") as f:
        subprocess.run(
            ["code", "--list-extensions"],
            stdout=f,
            check=True,
            shell=shell
        )

def main():
    operating_system = platform.system()
    home = os.path.expanduser("~")

    if operating_system == "Windows":
        dotfiles_dir = "C:/Git/dotfiles"
        shell = True
    else:
        dotfiles_dir = os.path.join(home, "Repositories/dotfiles")
        shell = False
    
    save_dir = os.path.join(dotfiles_dir, "VSCode")
    
    # Compare absolute paths
    current_working_dir = os.path.abspath(os.getcwd())
    expected_dir = os.path.abspath(dotfiles_dir)

    if current_working_dir == expected_dir:
        save_code_extensions(shell)
        print("Adding VS Code extensions…")
        subprocess.run(
            ["git", "add", "VSCode/code_extensions"],
            check=True,
            shell=shell
        )
    else:
        sys.exit(f"Error: script must be run from {expected_dir} (current directory is {current_working_dir})")

if __name__ == "__main__":
    main()
