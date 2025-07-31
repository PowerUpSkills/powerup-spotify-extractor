from .firefox_utils import find_firefox_profile_and_executable
from pathlib import Path
import pandas as pd
from playwright.sync_api import sync_playwright

def extract_liked_songs():
    """Extract liked songs from Spotify and save to CSV."""
    profile_path, executable_path = find_firefox_profile_and_executable()
    downloads = Path.home() / "Downloads" / "spotify_liked_songs.csv"

    with sync_playwright() as p:
        browser = p.firefox.launch_persistent_context(
            user_data_dir=str(profile_path),
            executable_path=executable_path,
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
