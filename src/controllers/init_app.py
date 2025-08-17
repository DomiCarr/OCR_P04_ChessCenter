"""init_app.py"""

import os
from config import DATA_DIRECTORY_PATH


def init_app():
    """create the data directory if not exist"""
    os.makedirs(DATA_DIRECTORY_PATH, exist_ok=True)
