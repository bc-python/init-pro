#!/usr/bin/env python3

# ----------------- #
# -- EXTRA TOOLS -- #
# ----------------- #

from collections import defaultdict

from mistool.os_use import PPath

from .message import *


# --------------- #
# -- CONSTANTS -- #
# --------------- #

COOKIECUTTER_JSON = "cookiecutter.json"


# ------------------------ #
# -- PROJECTS AVAILABLE -- #
# ------------------------ #

def findpeufs(cookiecutter_temp, peuf_dir):
    global COOKIECUTTER_JSON

# Looking for all the cookiecutter.json files.
    templates = []

    for onepath in cookiecutter_temp.walk(
        "file::**{0}".format(COOKIECUTTER_JSON)
    ):
        templates.append(f"{onepath.parent - cookiecutter_temp}")

# Finding all the peuf files.
    peuf_files = defaultdict(list)

    for onepath in peuf_dir.walk("file::**.peuf"):
        if onepath.stem[0] != "_":
            relativepath = onepath.parent - peuf_dir

            peuf_files[f"{relativepath}"].append(onepath.name)


# Checking for folder error.
    illegal_peuf = set(peuf_files.keys()) - set(templates)

    if illegal_peuf:
        illegal_peuf = sorted(list(illegal_peuf))

        print()

        error(
            ["Peuf folder(s) without corresponding cookiecutter templates: "]
            +
            [f"    + {n}" for n in illegal_peuf]
        )

        print()

        exit(1)

# Job has been done.
    return peuf_files
