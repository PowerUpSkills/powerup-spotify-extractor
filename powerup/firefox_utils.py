import os
from pathlib import Path

def find_firefox_profile_and_executable():
    """Find the default Firefox profile directory and matching executable."""
    profile_base = Path.home() / "Library/Application Support/Firefox/Profiles"

    if not profile_base.exists():
        raise RuntimeError("Could not find Firefox profiles directory. Please make sure Firefox or Firefox Developer Edition is installed and has been run at least once.")

    # Get all available profiles
    all_profiles = [p for p in profile_base.iterdir() if p.is_dir()]

    # Firefox configurations: (profile_pattern, executable_path)
    # Prioritize regular Firefox for better Playwright compatibility
    firefox_configs = [
        # Regular Firefox profiles (better Playwright compatibility)
        (".default-release", "/Applications/Firefox.app/Contents/MacOS/firefox"),
        (".default", "/Applications/Firefox.app/Contents/MacOS/firefox"),
        # Firefox Developer Edition profiles (fallback)
        (".dev-edition-default", "/Applications/Firefox Developer Edition.app/Contents/MacOS/firefox")
    ]

    for profile_pattern, executable_path in firefox_configs:
        if not Path(executable_path).exists():
            continue

        # Look for profiles matching the pattern
        for profile in all_profiles:
            if profile.name.endswith(profile_pattern):
                return profile, executable_path

    raise RuntimeError("Could not find a default Firefox profile and executable. Please make sure Firefox or Firefox Developer Edition is installed and has been run at least once.")

def find_firefox_profile():
    """Find the default Firefox profile directory (for backward compatibility)."""
    profile, _ = find_firefox_profile_and_executable()
    return profile
