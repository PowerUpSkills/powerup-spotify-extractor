# 🎵 PowerUp Spotify Extractor

Extract your liked songs from Spotify and save them to CSV format with this easy-to-use command-line tool.

## ✨ Features

- 🎯 Extract all your liked songs from Spotify
- 📊 Save songs to CSV format with title, artist, and album information
- 🌐 Open Spotify liked songs directly in your browser
- 🖥️ Beautiful CLI interface with ASCII art
- 🔄 Automatic scrolling to load all songs
- 🦊 Uses your existing Firefox profile (no login required)

## 🚀 Quick Start

### Option 1: Install from PyPI (Recommended)

```bash
pip install powerup-spotify-extractor
```

After installation, run:
```bash
powerup-spotify
```

### Option 2: Install from Source

1. Clone the repository:
```bash
git clone https://github.com/PowerUpSkills/powerup-spotify-extractor.git
cd powerup-spotify-extractor
```

2. Install the package:
```bash
pip install -e .
```

3. Run the application:
```bash
powerup-spotify
```

### Option 3: Development Setup

1. Clone and navigate to the project:
```bash
git clone https://github.com/PowerUpSkills/powerup-spotify-extractor.git
cd powerup-spotify-extractor
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Install Playwright browsers:
```bash
playwright install firefox
```

4. Run directly:
```bash
python -m powerup.main
```

## 📋 Requirements

- Python 3.8 or higher
- Firefox browser installed
- Active Spotify account (logged in via Firefox)

## 🛠️ How It Works

1. The tool uses Playwright to automate Firefox
2. It accesses your existing Firefox profile (where you're logged into Spotify)
3. Navigates to your Spotify liked songs page
4. Automatically scrolls to load all songs
5. Extracts song data (title, artist, album)
6. Saves everything to a CSV file in your Downloads folder

## 📁 Output

The extracted songs are saved as `spotify_liked_songs.csv` in your Downloads folder with the following columns:
- **title**: Song title
- **artist**: Artist name(s)
- **album**: Album name

## 🎮 Usage

When you run the tool, you'll see a menu with three options:

```
POWER UP — Spotify Favourite Songs Extractor

What would you like to do?

[1] Extract liked songs to CSV
[2] Open Spotify Liked Songs in browser
[3] Quit
```

Simply enter the number of your choice and press Enter.

## 🔧 Troubleshooting

### Firefox Profile Not Found
If you get an error about Firefox profile not found:
- Make sure Firefox is installed
- Open Firefox and log into Spotify at least once
- The tool looks for profiles in `~/Library/Application Support/Firefox/Profiles` (macOS)

### Playwright Issues
If you encounter Playwright-related errors:
```bash
playwright install firefox
```

### Permission Issues
If you get permission errors during installation:
```bash
pip install --user powerup-spotify-extractor
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👨‍💻 Author

**PowerUpSkills (Jannis)**
- Medium: [@PowerUpSkills](https://medium.com/@PowerUpSkills)
- GitHub: [@PowerUpSkills](https://github.com/PowerUpSkills)

## ⚠️ Disclaimer

This tool is for personal use only. Please respect Spotify's Terms of Service. The tool uses web automation to access your own data and does not violate any terms as it only accesses your personal liked songs that you already have access to.

## 🔗 Links

- [GitHub Repository](https://github.com/PowerUpSkills/powerup-spotify-extractor)
- [Report Issues](https://github.com/PowerUpSkills/powerup-spotify-extractor/issues)
- [Author's Medium](https://medium.com/@PowerUpSkills)
