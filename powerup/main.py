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
    """Display the main menu and handle user choices."""
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
    """Run the PowerUp Spotify Extractor."""
    main_menu()

if __name__ == "__main__":
    app()
