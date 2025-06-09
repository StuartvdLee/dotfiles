from pathlib import Path

src = Path("~/Repositories/dotfiles/Git/.gitconfig").expanduser()
dst = Path("~/.gitconfig").expanduser()

# Creates the symlink
dst.symlink_to(src)
print(f"Symlink created: {dst} → {src}")
