"""config.py"""

import os

# Dossier racine du projet
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

DATA_DIRECTORY_PATH = os.path.join(BASE_DIR, "data")
print(f"DATA_DIRECTORY_PATH: {DATA_DIRECTORY_PATH}")

PLAYERS_FILE_PATH = os.path.join(DATA_DIRECTORY_PATH, "players.json")
print(f"PLAYERS_FILE_PATH: {PLAYERS_FILE_PATH}")

TOURNAMENTS_FILE_PATH = os.path.join(DATA_DIRECTORY_PATH, "tournaments.json")
print(f"TOURNAMENTS_FILE_PATH: {TOURNAMENTS_FILE_PATH}")
