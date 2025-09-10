"""config.py - Configuration paths and project directories."""

import os

# Absolute path to the project root directory (one level above this file)
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# Directory where all data files (JSON) are stored
DATA_DIRECTORY_PATH = os.path.join(BASE_DIR, "data")

# Path to the JSON file storing player data
PLAYERS_FILE_PATH = os.path.join(DATA_DIRECTORY_PATH, "players.json")

# Path to the JSON file storing tournament data
TOURNAMENTS_FILE_PATH = os.path.join(DATA_DIRECTORY_PATH, "tournaments.json")
