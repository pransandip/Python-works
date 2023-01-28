import os
import json

BASE_DIR = ""
ASSETS_BIN = os.path.join(BASE_DIR, 'assets', 'bin')
ASSETS_IMAGES = os.path.join(BASE_DIR, 'assets', 'images')

LANGUAGE_STORE = json.load(open(os.path.join(ASSETS_BIN, "language.json"), encoding="utf-8"))
LANGUAGE_FLAG_IMAGES = os.path.join(ASSETS_IMAGES, 'flags')

CONFIG = os.path.join(ASSETS_BIN, "yms.config")
