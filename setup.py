from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="powerup-spotify-extractor",
    version="1.0.0",
    author="PowerUpSkills",
    author_email="jaydee.powerupskills@gmail.com",
    description="Extract your liked songs from Spotify and save them to CSV",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/PowerUpSkills/powerup-spotify-extractor",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Multimedia :: Sound/Audio",
        "Topic :: Utilities",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "powerup-spotify=powerup.main:app",
        ],
    },
    keywords="spotify, music, playlist, extractor, csv, automation",
    project_urls={
        "Bug Reports": "https://github.com/PowerUpSkills/powerup-spotify-extractor/issues",
        "Source": "https://github.com/PowerUpSkills/powerup-spotify-extractor",
        "Medium": "https://medium.com/@PowerUpSkills",
    },
)
