import os
from pathlib import Path

def find_firefox_profile():
    """Find the default Firefox profile directory."""
    base = Path.home() / "Library/Application Support/Firefox/Profiles"
    if not base.exists():
        raise FileNotFoundError("No Firefox profiles found.")

    for profile in base.iterdir():
        if profile.is_dir() and profile.name.endswith(".default-release"):
            return profile

    raise RuntimeError("Could not find a default Firefox profile.")
