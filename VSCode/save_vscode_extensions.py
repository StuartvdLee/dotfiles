import os
import subprocess

def main():
    # Determine paths
    home = os.path.expanduser("~")
    dotfiles_dir = os.path.join(home, "Repositories/dotfiles/VSCode")
    output_file = os.path.join(dotfiles_dir, "code_extensions")

    # Make sure the dotfiles directory exists
    os.makedirs(dotfiles_dir, exist_ok=True)

    print("Saving VSCode extensions...")

    # Run the `code --list-extensions` command and write its output to file
    with open(output_file, "w") as f:
        subprocess.run(
            ["code", "--list-extensions"],
            stdout=f,
            check=True
        )



        

if __name__ == "__main__":
    main()
