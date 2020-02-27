# #!/usr/bin/env python3

# ----------------- #
# -- EXTRA TOOLS -- #
# ----------------- #

from .message import *


# --------------- #
# -- CONSTANTS -- #
# --------------- #

# --------------------- #
# -- PROJECTS WANTED -- #
# --------------------- #

def chooseit(listofchoices):
    print()

    legalchoices = set('0')

    print("    0) Ignore this step.")

    for nb, kind in enumerate(listofchoices, 1):
        print(f"    {nb}) {kind}")

        legalchoices.add(str(nb))

    print()

    choices = input("Your choice(s): ")

    while True:
        choices = set(c.strip() for c in choices.split(' '))

        if choices <= legalchoices:
            break

        choices = input("Illegal choices. Retry: ")

    print()

    choices = [int(c) - 1 for c in sorted(choices)]

    return choices


def selections(peuf_dir, peuf_files):
# Which kind(s) of project to use ?
    sorted_keys = sorted(peuf_files.keys())

    if len(sorted_keys) == 1:
        choices = [0]

    else:
        print(
            "Which << KIND(S) >> of project(s) do you want to create ? "
            "Use spaces to separate your choices."
        )

        if -1 not in choices:
            choices = chooseit(sorted_keys)

# Which project(s) ?
    peuf_choosen = []
    lastkind     = ''

    for onechoice in choices:
        onekind = sorted_keys[onechoice]

        title(onekind)

        print(
            "Which << PROJECT(S) >> do you want to create ? "
            "Use spaces to separate your choices."
        )

        some_projects = peuf_files[onekind]

        choices = chooseit(some_projects)

        if -1 not in choices:
            for onechoice in choices:
                peuf_choosen.append(
                    f"{peuf_dir}/{onekind}/{some_projects[onechoice]}"
                )

# Job has been done.
    return peuf_choosen
