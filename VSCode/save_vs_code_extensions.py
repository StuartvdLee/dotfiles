import os
import subprocess
import argparse

def parse_args():
    parser = argparse.ArgumentParser(description="Save installed VSCode extensions to a file")
    parser.add_argument(
        "--file-dir",
        help="Directory to store the extensions file"
    )
    return parser.parse_args()

def main():
    args = parse_args()

    # Determine paths
    vs_code_dir = args.file_dir
    output_file = os.path.join(vs_code_dir, "code_extensions")

    # Make sure the dotfiles directory exists
    os.makedirs(vs_code_dir, exist_ok=True)

    print("Saving VSCode extensions...")

    # Run the `code --list-extensions` command and write its output to file
    with open(output_file, "w") as f:
        subprocess.run(
            ["code", "--list-extensions"],
            stdout=f,
            check=True,
            shell=True
        )        

if __name__ == "__main__":
    main()
