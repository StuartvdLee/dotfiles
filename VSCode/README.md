# VS Code

## settings.json

To use the `.settings.json` in this repository, perform the following steps:

**MacOS**
- Remove the `settings.json` from the `~/Library/"Application Support"/Code/User/` folder
- Add a symlink to the `settings.json` in this repository by running `ln -s ~/path/to/dotfiles/VSCode/settings.json ~/Library/"Application Support"/Code/User/settings.json` (**don't forget to point to the correct path**)

**Windows**
- Remove the `settings.json` from the `C:\Users\[USERNAME]\AppData\Roaming\Code\User\` folder
- Add a symlink to the `settings.json` in this repository by running `New-Item -ItemType SymbolicLink -Path "C:\Users\[USERNAME]\AppData\Roaming\Code\User\settings.json" -Target "C:\path\to\dotfiles\VSCode\settings.json"` (**don't forget to point to the correct path**)
