# VS Code MacOS

To use the `.settings.json` to the location of the `settings.json` in this repository, perform the following steps:

- Remove the `settings.json` from the `~/Library/"Application Support"/Code/User/` folder
- Add a symlink to the `settings.json` in this repository by running `ln -s ~/path/to/repository/VSCode/MacOS/settings.json ~/Library/"Application Support"/Code/User/settings.json` (**don't forget to point to the correct path**)