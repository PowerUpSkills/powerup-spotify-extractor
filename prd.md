### for GitHub repo:
https://github.com/PowerUpSkills/powerup-spotify-extractor

### Scope
- Extract liked songs from Spotify
- Save to CSV
- Open liked songs in browser
- Goal is to get your Favourite Songs playlist out of Spotify


### Directory structure (for GitHub repo):

# powerup_spotify_extractor/
# ├── powerup/
# │   ├── __init__.py
# │   ├── main.py            # CLI menu & ASCII
# │   ├── extractor.py       # Playwright automation
# │   ├── firefox_utils.py   # Profile detection
# │   └── ascii.py           # Banner string
# ├── setup.py
# ├── pyproject.toml
# ├── requirements.txt
# ├── README.md
# └── LICENSE

### powerup/main.py
import typer
from rich import print
from rich.console import Console
from rich.prompt import Prompt
from .ascii import BANNER
from .extractor import extract_liked_songs
import webbrowser
import sys

app = typer.Typer()
console = Console()

def main_menu():
    console.print(BANNER, style="cyan")
    print("[bold green]\nPOWER UP — Spotify Favourite Songs Extractor[/bold green]\n")
    print("What would you like to do?\n")
    print("[1] Extract liked songs to CSV")
    print("[2] Open Spotify Liked Songs in browser")
    print("[3] Quit")

    choice = Prompt.ask("\nEnter a number", choices=["1", "2", "3"])
    if choice == "1":
        extract_liked_songs()
    elif choice == "2":
        webbrowser.open("https://open.spotify.com/collection/tracks")
    else:
        print("\n[bold yellow]Find more hacks by me on Medium:[/bold yellow]")
        print("👉 https://medium.com/@PowerUpSkills\n")
        print("– Jannis\n")
        sys.exit()

@app.command()
def run():
    main_menu()

if __name__ == "__main__":
    app()

### powerup/ascii.py
BANNER = '''
:::::::::   ::::::::  :::       ::: :::::::::: :::::::::       :::    ::: :::::::::       
:+:    :+: :+:    :+: :+:       :+: :+:        :+:    :+:      :+:    :+: :+:    :+:      
+:+    +:+ +:+    +:+ +:+       +:+ +:+        +:+    +:+      +:+    +:+ +:+    +:+      
+#++:++#+  +#+    +:+ +#+  +:+  +#+ +#++:++#   +#++:++#:       +#+    +:+ +#++:++#+       
+#+        +#+    +#+ +#+ +#+#+ +#+ +#+        +#+    +#+      +#+    +#+ +#+             
#+#        #+#    #+#  #+#+# #+#+#  #+#        #+#    #+#      #+#    #+# #+#             
###         ########    ###   ###   ########## ###    ###       ########  ###             
 ::::::::  :::    ::: ::::::::::: :::        :::        ::::::::                          
:+:    :+: :+:   :+:      :+:     :+:        :+:       :+:    :+:                         
+:+        +:+  +:+       +:+     +:+        +:+       +:+                                
+#++:++#++ +#++:++        +#+     +#+        +#+       +#++:++#++                         
       +#+ +#+  +#+       +#+     +#+        +#+              +#+                         
#+#    #+# #+#   #+#      #+#     #+#        #+#       #+#    #+#                         
 ########  ###    ### ########### ########## ########## ########                           
'''

### powerup/firefox_utils.py
import os
from pathlib import Path

def find_firefox_profile():
    base = Path.home() / "Library/Application Support/Firefox/Profiles"
    if not base.exists():
        raise FileNotFoundError("No Firefox profiles found.")

    for profile in base.iterdir():
        if profile.is_dir() and profile.name.endswith(".default-release"):
            return profile

    raise RuntimeError("Could not find a default Firefox profile.")

### powerup/extractor.py
from .firefox_utils import find_firefox_profile
from pathlib import Path
import pandas as pd
from playwright.sync_api import sync_playwright

def extract_liked_songs():
    profile_path = find_firefox_profile()
    downloads = Path.home() / "Downloads" / "spotify_liked_songs.csv"

    with sync_playwright() as p:
        browser = p.firefox.launch_persistent_context(
            user_data_dir=str(profile_path),
            headless=False,
            viewport={"width": 1280, "height": 800},
        )
        page = browser.new_page()
        page.goto("https://open.spotify.com/collection/tracks")
        page.wait_for_timeout(5000)

        # Scroll to load more songs
        prev_height = 0
        while True:
            page.mouse.wheel(0, 10000)
            page.wait_for_timeout(1000)
            curr_height = page.evaluate("document.scrollingElement.scrollTop")
            if curr_height == prev_height:
                break
            prev_height = curr_height

        rows = page.eval_on_selector_all(
            '[data-testid="tracklist-row"]',
            '''nodes => nodes.map(n => {
                const cells = n.querySelectorAll('[data-testid="cell-inner-text"]');
                return {
                    title: cells[0]?.innerText || '',
                    artist: cells[1]?.innerText || '',
                    album: cells[2]?.innerText || ''
                }
            })'''
        )

        df = pd.DataFrame(rows)
        df.to_csv(downloads, index=False)
        print(f"\n[green]Saved {len(df)} liked songs to:[/green] {downloads}\n")

        browser.close()
