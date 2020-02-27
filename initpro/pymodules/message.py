#!/usr/bin/env python3


# --------------- #
# -- CONSTANTS -- #
# --------------- #

ERROR_NB = 0


# -------------------------- #
# -- FUNCTIONS -- #
# -------------------------- #

def error(texts):
    global ERROR_NB

    ERROR_NB += 1

    print(f"--> ERROR {ERROR_NB}")

    for onetext in texts:
        print(f"    {onetext}")


def title(text):
    deco = "="*len(text)

    print(
        deco,
        text,
        deco,
        "",
        sep = "\n"
    )
