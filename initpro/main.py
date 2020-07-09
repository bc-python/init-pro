#!/usr/bin/env python3

# ----------------- #
# -- EXTRA TOOLS -- #
# ----------------- #

from mistool.os_use import PPath

from pymodules.available import *
from pymodules.wanted import *
from pymodules.cookify import *


# --------------- #
# -- CONSTANTS -- #
# --------------- #

THIS_DIR = PPath(__file__).parent

COOKIECUTTER_TEMP = THIS_DIR / "cookiecutter-templates"
PEUF_DIR          = THIS_DIR / "peuf-init"


# ----------------- #
# -- CLI MANAGER -- #
# ----------------- #

peuf_files = findpeufs(COOKIECUTTER_TEMP, PEUF_DIR)

if not peuf_files:
    print()
    print('Nothing found !\n')
    exit(0)

peuf_choosen = selections(PEUF_DIR, peuf_files)

cookifyles(
    COOKIECUTTER_TEMP,
    PEUF_DIR,
    [PPath(pc) for pc in peuf_choosen]
)
