# VS Code

## Prerequisites
- Python 3 has to be installed (for extension management)

## settings.json
To use the `.settings.json` in this repository, perform the following steps:

### MacOS
- Remove the `settings.json` from the `~/Library/"Application Support"/Code/User/` folder
- Add a symlink to the `settings.json` in this repository by running `ln -s ~/path/to/dotfiles/VSCode/settings.json ~/Library/"Application Support"/Code/User/settings.json` (**don't forget to point to the correct path**)

### Windows
- Remove the `settings.json` from the `C:\Users\[USERNAME]\AppData\Roaming\Code\User\` folder
- Add a symlink to the `settings.json` in this repository by running `New-Item -ItemType SymbolicLink -Path "C:\Users\[USERNAME]\AppData\Roaming\Code\User\settings.json" -Target "C:\path\to\dotfiles\VSCode\settings.json"` (**don't forget to point to the correct path**)

## Extensions

### Saving extensions through pre-commit
Extensions are automatically saved to `code_extensions` through [pre-commit](https://pre-commit.com/). Follow the [Quick start](https://pre-commit.com/#quick-start) to install pre-commit.

### Saving extensions manually
Extensions can also be saved manually by running the `save_vs_code_extensions.py` script:

#### MacOs
 - `python3 VSCode/save_vs_code_extensions.py --file-dir ~/path/to/dotfiles/VSCode` (**don't forget to point to the correct path**)

#### Windows
 - `python .\VSCode\save_vs_code_extensions.py --file-dir C:\path\to\dotfiles\VSCode\` (**don't forget to point to the correct path**)

### Installation of extensions

To install extensions from `code_extensions`, perform the following steps:

#### MacOS
- Run `python3 VSCode/install_extensions.py`

#### Windows
- Run `python .\VSCode\install_extensions.py`

test
