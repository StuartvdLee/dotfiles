import os
import subprocess
import sys

def save_code_extensions():
    """Save the list of installed VSCode extensions to ./VSCode/code_extensions"""
    print("Saving VSCode extensions…")
    with open("code_extensions", "w") as f:
        subprocess.run(
            ["code", "--list-extensions"],
            stdout=f,
            check=True
        )

def main():
    home = os.path.expanduser("~")
    dotfiles_dir = os.path.join(home, "Repositories/dotfiles")

    # Compare absolute paths
    current_working_dir = os.path.abspath(os.getcwd())
    expected_dir = os.path.abspath(dotfiles_dir)

    if current_working_dir == expected_dir:
        save_code_extensions()
        print("Adding code_extensions to git…")
        subprocess.run(
            ["git", "add", "code_extensions"],
            check=True
        )
    else:
        sys.exit(f"Error: script must be run from {expected_dir} (current directory is {current_working_dir})")

if __name__ == "__main__":
    main()
