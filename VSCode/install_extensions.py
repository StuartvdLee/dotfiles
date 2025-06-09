import os
import subprocess
import sys
import platform

def command_output(cmd, shell):
    """Run a command and return its stdout as a list of stripped lines."""
    try:
        result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, check=True, text=True, shell=shell)
        return [line.strip() for line in result.stdout.splitlines() if line.strip()]
    except subprocess.CalledProcessError:
        return []

def main():
    operating_system = platform.system()

    if operating_system == "Windows":
        extensions_path = "C:/git/dotfiles/VSCode/code_extensions"
        shell = True
    else:
        extensions_path = os.path.expanduser("~/Repositories/dotfiles/VSCode/code_extensions")
        shell = False

    # Load saved extensions
    if not os.path.isfile(extensions_path):
        sys.exit(f"No saved extensions file at {extensions_path!r}")

    with open(extensions_path, "r") as f:
        saved_extensions = sorted(line.strip() for line in f if line.strip())

    # Get currently installed extensions
    installed_extensions = sorted(command_output(["code", "--list-extensions"], shell))

    # Compute which saved extensions are not installed
    missing_extensions = [ext for ext in saved_extensions if ext not in installed_extensions]

    print("Checking for uninstalled VS Code extensions...")

    if not missing_extensions:
        print("No uninstalled VS Code extensions found!\r\n")
    else:
        print(f"found {len(missing_extensions)}\r\n")
        for ext in missing_extensions:
            # print(f"Installing {ext}...")
            try:
                subprocess.run(["code", "--install-extension", ext], check=True, shell=shell)
            except subprocess.CalledProcessError:
                print(f"Failed to install {ext}", file=sys.stderr)
        print("Done!")

if __name__ == "__main__":
    main()

