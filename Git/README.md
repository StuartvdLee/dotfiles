# Git

## Prerequisites
- Python 3

## .gitconfig
To set the global `.gitconfig` to the location of the `.gitconfig` in this repository, perform the following steps:

### MacOS
- Remove the `.gitconfig` from the HOME folder
- Run `python3 Git/set_gitconfig.py`

### Windows
- Run `python .\Git\set_gitconfig.py

Fill in your name and e-mail in the `.gitconfig` in the repository file and you should be good to go!

### Remarks
The `.gitconfig` file was removed from tracking in git to prevent changes (such as adding your name or e-mail) from being pushed to the remote. This was done by running `git update-index --skip-worktree Git/.gitconfig`.

If changes are made to the `.gitconfig` file that need to be pushed to the remote, simply run `git update-index --no-skip-worktree Git/.gitconfig` to include these changes. ***Don't forget to revert this again!***
