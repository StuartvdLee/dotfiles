import os
import subprocess
import sys

def command_output(cmd):
    """Run a command and return its stdout as a list of stripped lines."""
    try:
        result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, check=True, text=True)
        return [line.strip() for line in result.stdout.splitlines() if line.strip()]
    except subprocess.CalledProcessError:
        return []

def main():
    # Load saved extensions
    extensions_path = os.path.expanduser("~/Repositories/dotfiles/VSCode/code_extensions")
    if not os.path.isfile(extensions_path):
        sys.exit(f"No saved extensions file at {extensions_path!r}")

    with open(extensions_path, "r") as f:
        saved_extensions = sorted(line.strip() for line in f if line.strip())

    # Get currently installed extensions
    installed_extensions = sorted(command_output(["code", "--list-extensions"]))

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
                subprocess.run(["code", "--install-extension", ext], check=True)
            except subprocess.CalledProcessError:
                print(f"Failed to install {ext}", file=sys.stderr)
        print("Done!")

if __name__ == "__main__":
    main()

