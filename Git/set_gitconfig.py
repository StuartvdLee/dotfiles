import os
from pathlib import Path

src = Path("~/Repositories/dotfiles/Git/.gitconfig").expanduser()
dst = Path("~/.gitconfig").expanduser()

print(dst)

# Creates the symlink
os.symlink(src, dst)
print(f"Symlink created: {dst} → {src}")
