#!/usr/bin/env python3

# ----------------- #
# -- EXTRA TOOLS -- #
# ----------------- #

from json import dumps as json_dumps

from mistool.os_use import cd, PPath, runthis
from mistool.term_use import Step
from orpyste.data import ReadBlock

from .message import *


# --------------- #
# -- CONSTANTS -- #
# --------------- #


# ----------------- #
# -- LOCAL TOOLS -- #
# ----------------- #

MAIN_STEPS = Step()


# ------------------ #
# -- PEUF TO JSON -- #
# ------------------ #

def projects_to_do(
    cookiecutter_temp,
    all_peuf_choosen
):
    projects_to_do = []
    already_build  = []

    for onepeuf in all_peuf_choosen:
        with ReadBlock(
            content = onepeuf,
            mode    = {
                "keyval:: =": "project"
            }
        ) as datas:
            flatdict = datas.mydict("std nosep nonb")['project']

# The key 'name' becomes 'project_name':
            flatdict['project_name'] = flatdict['name']
            del flatdict['name']


# We have to listify values of keys starting by _.
            for k, v in flatdict.items():
# Launches uses a very specific ways to store values.
                if k == "_launched_by_factory":
                    command_n_patterns = [
                        p.strip()
                        for p in v.split(":launch:")
                    ]

                    command_n_patterns[1] = [
                        p.strip()
                        for p in command_n_patterns[1].split("|")
                    ]


                    flatdict[k] = command_n_patterns

# Keys using a coma sperated syntax in the peuf file.
                elif k in [
                    "_authors",
                    "_for_test",
                    "_for_factory"
                ]:
                    v = [
                        [p.strip() for p in x.split(",")]
                        for x in v.split(";")
                    ]

                    if k == "_authors":
                        v = [
                            [', '.join(x[:-1]), x[-1]]
                            for x in v
                        ]

                    flatdict[k] = v

# Ready to use list value.
                elif k[0] == "_":
                    flatdict[k] = [x.strip() for x in v.split(";")]

# Does we have nothing ?
            newprojectpath = cookiecutter_temp \
                           / onepeuf.parent.parent.name \
                           / flatdict['project_name']

            if newprojectpath.is_dir():
                already_build.append(newprojectpath)

# We have something to do.
            else:
                projects_to_do.append({
                    'json': flatdict,
                    'lang': onepeuf.parent.parent.name,
                    'kind': onepeuf.parent.name
                })

# Some errors have been found.
    if already_build:
        error([
            "Local project already build (erase it if you want to rebuild it): "
        ] + [
            f"    + {p}" for p in already_build
        ] + [
            '',
            "Nothing has been done !"
        ])

        exit(1)

# Everything is ok.
    return projects_to_do


def cookifyles(
    cookiecutter_temp,
    all_peuf_choosen
):
    title("LET'S WORK...")

# Let's add the new json files.
    allprojects = projects_to_do(
        cookiecutter_temp,
        all_peuf_choosen
    )

    for project in allprojects:
        SUB_STEPS = Step(
            start = 1,
            textit = lambda n, t: f"    {chr(96 + n)}/ {t}"
        )

        projectreldir = f"{project['lang']}" \
                      + f"/{project['json']['project_name']}"

        MAIN_STEPS(f"Building {projectreldir}")

# Build the json file.
        SUB_STEPS("Updating the json file.")

        jsonpath = cookiecutter_temp \
                 / project['lang'] \
                 / project['kind'] \
                 / 'cookiecutter.json'

        with jsonpath.open(
            encoding = 'utf-8',
            mode     = 'w'
        ) as f:
            f.write(json_dumps(project['json']))

# Call of cookiecutter.
        SUB_STEPS("Trying to launch cookiecutter.")

        with cd(cookiecutter_temp / project['lang']):
            try:
                runthis(
                    f"cookiecutter --no-input {project['kind']}",
                    showoutput = True
                )

            except Exception as e:
                print('\nCookiecutter fails. See above why.')
                exit(1)

        SUB_STEPS("cookiecutter has done its local job.")

# Moving, or not, the folder.
        SUB_STEPS("Do not forget to move the new folder.")

# Open the cookie templates folder.
    print()

    title(f'Opening folder of the cookie templates')

    runthis(f'open  "{cookiecutter_temp}"')

    print("Here are all the starting project build.")

    SUB_STEPS = Step(
        start = 1,
        textit = lambda n, t: f"    {n}: {t}"
    )

    for project in allprojects:
        SUB_STEPS(
            f"{project['lang']}/{project['json']['project_name']}"
        )

    print()
