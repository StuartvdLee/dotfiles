import ctypes
import platform
import winreg

from pathlib import Path

operating_system = platform.system()

if operating_system == "Windows":
    new_path = r"C:\Git\dotfiles\Git"

    # Write to HKCU\Environment
    with winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Environment", 0, winreg.KEY_SET_VALUE) as key:
        winreg.SetValueEx(key, "HOME", 0, winreg.REG_SZ, new_path)

    # Broadcast WM_SETTINGCHANGE so new shells & Explorer see it
    HWND_BROADCAST = 0xFFFF
    WM_SETTINGCHANGE = 0x001A
    ctypes.windll.user32.SendMessageW(HWND_BROADCAST, WM_SETTINGCHANGE, 0, "Environment")

    print("Set $Env:HOME to", new_path)	
else:
    src = Path("~/Repositories/dotfiles/Git/.gitconfig").expanduser()
    dst = Path("~/.gitconfig").expanduser()

    # Creates the symlink
    dst.symlink_to(src)
    print(f"Symlink created: {dst} → {src}")
